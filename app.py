import json
import os
from datetime import datetime
from functools import wraps
from flask import (Flask, render_template, request, redirect, url_for,
                   session, flash, jsonify, abort)
from werkzeug.security import generate_password_hash, check_password_hash

from data import DESTINATIONS
from reviews import get_reviews

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "user_data")
os.makedirs(DATA_DIR, exist_ok=True)
USERS_FILE = os.path.join(DATA_DIR, "users.json")

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "herroute-dev-secret-key")


# ---------- storage helpers ----------
def _load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_users(data):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def _empty_user_profile(name, email, phone=""):
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "password_hash": "",
        "preferences": {
            "travel_type": "Mountains, Beaches",
            "budget_range": "₹2,000 - ₹5,000 / day",
            "travel_style": "Solo",
        },
        "trips": [],            # planned + completed itineraries
        "saved": [],            # destination ids saved/wishlist
        "budgets": [],          # budget plans
        "emergency_contacts": [
            {"name": "Mom", "phone": "+91 98765 43210", "relation": "Family"},
        ],
    }


def get_current_user():
    email = session.get("user_email")
    if not email:
        return None
    users = _load_users()
    return users.get(email)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_email"):
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


# ---------- context ----------
@app.context_processor
def inject_globals():
    user = get_current_user()
    return {
        "current_user": user,
        "current_year": datetime.now().year,
        "app_name": "HerRoute",
        "tagline": "Your Route. Your Story. Your Freedom.",
    }


# ---------- auth ----------
@app.route("/")
def root():
    if session.get("user_email"):
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        users = _load_users()
        user = users.get(email)
        if user and check_password_hash(user.get("password_hash", ""), password):
            session["user_email"] = email
            flash(f"Welcome back, {user['name'].split()[0]}!", "success")
            nxt = request.args.get("next") or url_for("home")
            return redirect(nxt)
        flash("Invalid email or password.", "error")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        phone = (request.form.get("phone") or "").strip()
        password = request.form.get("password") or ""
        confirm = request.form.get("confirm") or ""
        if not (name and email and password):
            flash("Please fill all required fields.", "error")
        elif password != confirm:
            flash("Passwords do not match.", "error")
        elif len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
        else:
            users = _load_users()
            if email in users:
                flash("An account with this email already exists.", "error")
            else:
                profile = _empty_user_profile(name, email, phone)
                profile["password_hash"] = generate_password_hash(password)
                users[email] = profile
                _save_users(users)
                session["user_email"] = email
                flash("Account created. Welcome to HerRoute!", "success")
                return redirect(url_for("home"))
    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


# ---------- main pages ----------
@app.route("/home")
@login_required
def home():
    user = get_current_user()
    popular = DESTINATIONS[:6]
    safe_quick = DESTINATIONS[:4]
    completed = [t for t in user["trips"] if t.get("status") == "completed"]
    planned = [t for t in user["trips"] if t.get("status") == "planned"]
    total_budget = sum(t.get("budget", 0) for t in user["trips"])
    return render_template(
        "home.html",
        popular=popular,
        safe_quick=safe_quick,
        completed_count=len(completed),
        planned_count=len(planned),
        total_budget=total_budget,
    )


@app.route("/explore")
@login_required
def explore():
    category = request.args.get("category", "All")
    rating = request.args.get("rating", "All")
    items = list(DESTINATIONS)
    if category and category != "All":
        items = [d for d in items if d["category"].lower() == category.lower()]
    if rating and rating != "All":
        try:
            min_rating = float(rating)
            items = [d for d in items if d["rating"] >= min_rating]
        except ValueError:
            pass
    categories = ["All", "Mountains", "Beaches", "Cities", "Heritage", "Adventure"]
    rating_options = ["All", "4.5", "4.0", "3.5"]
    return render_template(
        "explore.html",
        destinations=items,
        categories=categories,
        rating_options=rating_options,
        active_category=category,
        active_rating=rating,
    )


@app.route("/destination/<dest_id>")
@login_required
def destination_detail(dest_id):
    dest = next((d for d in DESTINATIONS if d["id"] == dest_id), None)
    if not dest:
        abort(404)
    reviews_block = get_reviews(dest)
    return render_template("destination.html", dest=dest, reviews=reviews_block)


# ---------- itinerary ----------
@app.route("/itinerary", methods=["GET", "POST"])
@login_required
def itinerary():
    users = _load_users()
    email = session["user_email"]
    user = users[email]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "create":
            trip = {
                "id": f"trip_{int(datetime.now().timestamp())}",
                "name": request.form.get("trip_name", "New Trip"),
                "start_date": request.form.get("start_date", ""),
                "end_date": request.form.get("end_date", ""),
                "destination": request.form.get("destination", ""),
                "budget": int(request.form.get("budget") or 0),
                "status": "planned",
                "days": [],
            }
            user["trips"].append(trip)
            _save_users(users)
            flash("Trip created.", "success")
            return redirect(url_for("itinerary", trip=trip["id"]))
        elif action == "add_day":
            trip_id = request.form.get("trip_id")
            for t in user["trips"]:
                if t["id"] == trip_id:
                    day_no = len(t["days"]) + 1
                    t["days"].append({
                        "day": day_no,
                        "date": request.form.get("date", ""),
                        "activities": [],
                    })
                    break
            _save_users(users)
            return redirect(url_for("itinerary", trip=trip_id))
        elif action == "add_activity":
            trip_id = request.form.get("trip_id")
            day_no = int(request.form.get("day_no") or 0)
            for t in user["trips"]:
                if t["id"] == trip_id:
                    for d in t["days"]:
                        if d["day"] == day_no:
                            d["activities"].append({
                                "time": request.form.get("time", ""),
                                "title": request.form.get("title", ""),
                                "note": request.form.get("note", ""),
                            })
                            break
                    break
            _save_users(users)
            return redirect(url_for("itinerary", trip=trip_id))
        elif action == "complete":
            trip_id = request.form.get("trip_id")
            for t in user["trips"]:
                if t["id"] == trip_id:
                    t["status"] = "completed"
                    break
            _save_users(users)
            flash("Trip marked as completed.", "success")
            return redirect(url_for("itinerary"))
        elif action == "delete":
            trip_id = request.form.get("trip_id")
            user["trips"] = [t for t in user["trips"] if t["id"] != trip_id]
            _save_users(users)
            flash("Trip deleted.", "success")
            return redirect(url_for("itinerary"))

    selected_id = request.args.get("trip")
    selected = None
    if selected_id:
        selected = next((t for t in user["trips"] if t["id"] == selected_id), None)
    elif user["trips"]:
        selected = user["trips"][-1]
    return render_template(
        "itinerary.html",
        trips=user["trips"],
        selected=selected,
        destinations=DESTINATIONS,
    )


# ---------- budget ----------
@app.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    users = _load_users()
    email = session["user_email"]
    user = users[email]

    if request.method == "POST":
        action = request.form.get("action")
        if action == "create":
            plan = {
                "id": f"bud_{int(datetime.now().timestamp())}",
                "trip_name": request.form.get("trip_name", "New Budget"),
                "destination": request.form.get("destination", ""),
                "total": int(request.form.get("total") or 0),
                "items": [],
            }
            user["budgets"].append(plan)
            _save_users(users)
            return redirect(url_for("budget", plan=plan["id"]))
        elif action == "add_item":
            plan_id = request.form.get("plan_id")
            for p in user["budgets"]:
                if p["id"] == plan_id:
                    p["items"].append({
                        "category": request.form.get("category", "Other"),
                        "label": request.form.get("label", ""),
                        "amount": int(request.form.get("amount") or 0),
                    })
                    break
            _save_users(users)
            return redirect(url_for("budget", plan=plan_id))
        elif action == "delete_plan":
            plan_id = request.form.get("plan_id")
            user["budgets"] = [p for p in user["budgets"] if p["id"] != plan_id]
            _save_users(users)
            return redirect(url_for("budget"))

    plan_id = request.args.get("plan")
    selected = None
    if plan_id:
        selected = next((p for p in user["budgets"] if p["id"] == plan_id), None)
    elif user["budgets"]:
        selected = user["budgets"][-1]
    return render_template("budget.html", plans=user["budgets"], selected=selected,
                           destinations=DESTINATIONS)


# ---------- emergency ----------
@app.route("/emergency", methods=["GET", "POST"])
@login_required
def emergency():
    users = _load_users()
    email = session["user_email"]
    user = users[email]
    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            user["emergency_contacts"].append({
                "name": request.form.get("name", ""),
                "phone": request.form.get("phone", ""),
                "relation": request.form.get("relation", "Friend"),
            })
            _save_users(users)
        elif action == "delete":
            idx = int(request.form.get("idx") or -1)
            if 0 <= idx < len(user["emergency_contacts"]):
                user["emergency_contacts"].pop(idx)
                _save_users(users)
        return redirect(url_for("emergency"))

    national_numbers = [
        {"label": "Police", "phone": "100", "icon": "shield"},
        {"label": "Women Helpline", "phone": "1091", "icon": "alert"},
        {"label": "Ambulance", "phone": "102", "icon": "plus"},
        {"label": "Fire Service", "phone": "101", "icon": "fire"},
        {"label": "National Emergency", "phone": "112", "icon": "siren"},
        {"label": "Tourist Helpline", "phone": "1363", "icon": "compass"},
    ]
    return render_template("emergency.html",
                           contacts=user["emergency_contacts"],
                           national_numbers=national_numbers)


# ---------- safety ----------
@app.route("/safety")
@login_required
def safety():
    tips = [
        {"title": "Plan Ahead",
         "text": "Research your destination thoroughly and plan your route, stays and transport before you go."},
        {"title": "Share Your Itinerary",
         "text": "Always share your travel plans, hotel address and daily schedule with someone you trust."},
        {"title": "Stay Connected",
         "text": "Keep your phone charged, carry a power bank and have a local SIM or international roaming."},
        {"title": "Avoid Isolated Areas",
         "text": "Avoid lonely or poorly lit areas, especially at night. Stick to well-populated routes."},
        {"title": "Trust Your Instincts",
         "text": "If something feels wrong, leave the situation immediately. Your gut is usually right."},
        {"title": "Carry Essentials",
         "text": "Pepper spray, a whistle, copies of ID, and a small first-aid kit should always be with you."},
        {"title": "Dress Appropriately",
         "text": "Respect the local culture by dressing modestly. It also helps you blend in and avoid unwanted attention."},
        {"title": "Use Verified Stays",
         "text": "Book accommodations from trusted platforms and prefer female-friendly or women-only stays."},
        {"title": "Beware of Drinks",
         "text": "Never leave your food or drink unattended. Order it yourself and keep an eye on it."},
    ]
    return render_template("safety.html", tips=tips)


# ---------- saved ----------
@app.route("/saved", methods=["GET", "POST"])
@login_required
def saved():
    users = _load_users()
    email = session["user_email"]
    user = users[email]
    if request.method == "POST":
        dest_id = request.form.get("dest_id")
        action = request.form.get("action")
        if action == "toggle" and dest_id:
            if dest_id in user["saved"]:
                user["saved"].remove(dest_id)
            else:
                user["saved"].append(dest_id)
            _save_users(users)
        return redirect(request.referrer or url_for("saved"))

    saved_dests = [d for d in DESTINATIONS if d["id"] in user["saved"]]
    planned = [t for t in user["trips"] if t.get("status") == "planned"]
    return render_template("saved.html",
                           saved_dests=saved_dests,
                           planned_trips=planned)


# ---------- profile ----------
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    users = _load_users()
    email = session["user_email"]
    user = users[email]
    if request.method == "POST":
        user["name"] = request.form.get("name", user["name"])
        user["phone"] = request.form.get("phone", user["phone"])
        user["preferences"]["travel_type"] = request.form.get(
            "travel_type", user["preferences"]["travel_type"])
        user["preferences"]["budget_range"] = request.form.get(
            "budget_range", user["preferences"]["budget_range"])
        user["preferences"]["travel_style"] = request.form.get(
            "travel_style", user["preferences"]["travel_style"])
        _save_users(users)
        flash("Profile updated.", "success")
        return redirect(url_for("profile"))

    completed = [t for t in user["trips"] if t.get("status") == "completed"]
    planned = [t for t in user["trips"] if t.get("status") == "planned"]
    return render_template("profile.html",
                           saved_count=len(user["saved"]),
                           planned_count=len(planned),
                           completed_count=len(completed))


# ---------- api: SOS share ----------
@app.route("/api/sos", methods=["POST"])
@login_required
def api_sos():
    user = get_current_user()
    contacts = user.get("emergency_contacts", [])
    return jsonify({
        "ok": True,
        "message": f"SOS alert (simulated) sent to {len(contacts)} contact(s).",
        "contacts": [c["name"] for c in contacts],
        "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
    })


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
