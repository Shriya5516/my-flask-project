# HerRoute — Solo Female Travel Planner (Flask)

A B.Tech CS mini-project: a safe, friendly travel planner web app for solo
female travellers in India. Built with **Python Flask + HTML/CSS/JS**.

## Features

- Working signup / login / logout (passwords are hashed)
- Home dashboard with trip + budget stats
- 20 hand-picked solo-girl-friendly destinations across India (real images)
- Destination detail pages with:
  - Girl-friendly hotels & stays
  - Hospitals near the hotel
  - Police stations near the hotel
  - Rescue / women / tourism helplines
  - **Real-time traveller reviews** (Google Maps when an API key is set,
    curated community reviews otherwise)
- Itinerary planner (multi-day, with activities)
- Budget planner (per-trip breakdown)
- Emergency contacts + SOS share-location button
- Safety tips library
- Saved trips / wishlist
- Profile + preferences

## Project structure

```
flask_app/
├── app.py                 # Flask routes (auth, pages, api/sos)
├── data.py                # 20 destinations with hotels/hospitals/police/rescue
├── reviews.py             # Real-time Google Maps reviews + cached fallback
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── static/
│   ├── css/style.css      # Purple-gradient design system
│   ├── js/main.js         # SOS button, share location
│   └── images/
│       ├── logo.jpeg
│       └── destinations/  # Local hero image for each destination
└── templates/             # Jinja templates
    ├── base.html
    ├── login.html  signup.html
    ├── home.html  explore.html  destination.html
    ├── itinerary.html  budget.html
    ├── emergency.html  safety.html
    ├── saved.html  profile.html
    └── 404.html
```

## How to run in VS Code (step by step)

> Works on Windows, Mac and Linux.

### 1. Install Python 3.10 or later
Download from <https://www.python.org/downloads/>. On Windows, **tick "Add Python to PATH"** during install.

### 2. Open the project
1. Open VS Code.
2. `File → Open Folder…` → choose the `flask_app` folder.
3. When VS Code asks, install the **Python extension by Microsoft**.

### 3. Create a virtual environment (recommended)
Open the integrated terminal (`Ctrl + ` ` ` or `View → Terminal`) and run:

**Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. (Optional) Set environment variables

| Variable | What it does |
|---|---|
| `SESSION_SECRET` | Flask session signing key. A default is used if unset. |
| `GOOGLE_PLACES_API_KEY` | If set, destination pages show **real-time Google Maps reviews**. Without it, curated traveller reviews are shown. |
| `PORT` | Port to run on (default `5000`). |

To get a Google Places API key:
1. Go to <https://console.cloud.google.com/>.
2. Create / pick a project → **APIs & Services → Library**.
3. Enable **Places API** (the new "Places API" or the legacy one — both work).
4. **Credentials → + Create credentials → API key**.
5. Restrict the key to "Places API" for safety.

Set it like this:

**Windows (PowerShell)**
```powershell
$env:GOOGLE_PLACES_API_KEY = "your-key-here"
```

**Mac / Linux**
```bash
export GOOGLE_PLACES_API_KEY="your-key-here"
```

### 6. Run the app
```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

Open <http://localhost:5000> in your browser. Sign up with any email + password (≥ 6 chars) and you're in.

### 7. Run from the VS Code "Run" button
- Open `app.py`.
- Click the **▶ Run** arrow at the top right of VS Code.
- VS Code will use the venv Python and launch the app in the terminal.

## Notes

- All user data (signup info, trips, budgets, contacts) is saved as JSON in
  `flask_app/user_data/users.json` so nothing is lost between restarts.
- Destination images are saved locally inside `static/images/destinations/`
  so the app works completely offline.
- Reviews are cached for 24 hours in `user_data/reviews_cache.json` to avoid
  hitting Google's quota.
