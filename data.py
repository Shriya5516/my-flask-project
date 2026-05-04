"""
HerRoute — destination dataset.
20 hand-picked, solo-girl-friendly destinations across India.

Images are stored locally under /static/images/destinations/<id>.jpg
so that the app works offline without any third-party hot-linking.
"""


def _d(id, name, category, state, rating, reviews, safety, best, ideal, budget,
       desc, tips, hotels, hospitals, police, rescue, google_query=None):
    return {
        "id": id,
        "name": name,
        "category": category,
        "state": state,
        "rating": rating,
        "reviews": reviews,
        "safety_level": safety,
        "best_time": best,
        "ideal_for": ideal,
        "avg_budget": budget,
        "image": f"/static/images/destinations/{id}.jpg",
        "description": desc,
        "tips": tips,
        "google_query": google_query or f"{name} {state} India tourism",
        "nearby": {
            "hotels": hotels,
            "hospitals": hospitals,
            "police": police,
            "rescue": rescue,
        },
    }


DESTINATIONS = [
    _d(
        id="goa", name="Goa", category="Beaches", state="Goa",
        rating=4.8, reviews=325, safety="Very Safe",
        best="Nov - Feb", ideal="Solo, Friends, Adventure",
        budget="₹2,000 - ₹5,000 / day",
        desc="Goa is famous for its sunny beaches, friendly locals and laid-back cafes. A perfect destination for solo girls who want to unwind, meet other travellers and dance the night away in safe, well-lit beach shacks.",
        tips="Stay in well-reviewed properties in North Goa (Anjuna, Vagator, Assagao). Use pre-paid taxis or GoaMiles after dark.",
        hotels=[
            {"name": "Zostel Goa (Female Dorms)", "phone": "+91 81308 70008", "distance": "0.4 km from Anjuna beach", "rating": 4.6, "tag": "Female-only dorm"},
            {"name": "The Hosteller Anjuna", "phone": "+91 91376 21270", "distance": "0.7 km from beach", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Manipal Hospital, Goa", "phone": "+91 832 274 5555", "distance": "3.2 km from hotel"},
            {"name": "Healthway Hospital", "phone": "+91 832 247 0000", "distance": "5.4 km from hotel"},
        ],
        police=[
            {"name": "Anjuna Police Station", "phone": "+91 832 227 3233", "distance": "1.1 km from hotel"},
            {"name": "Calangute Police Station", "phone": "+91 832 227 6488", "distance": "4.8 km from hotel"},
        ],
        rescue=[
            {"name": "Drishti Marine Lifeguards", "phone": "+91 832 651 9555", "distance": "0.6 km"},
            {"name": "Goa Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="manali", name="Manali", category="Mountains", state="Himachal Pradesh",
        rating=4.7, reviews=290, safety="Very Safe",
        best="Mar - Jun, Oct - Feb", ideal="Solo, Trekking, Snow",
        budget="₹1,500 - ₹4,000 / day",
        desc="A scenic mountain town surrounded by snow-capped peaks, pine forests and the rushing Beas river. A backpacker favourite with safe hostels, cosy cafes and well-trodden trekking circuits.",
        tips="Old Manali and Vashisht have plenty of female-friendly hostels. Avoid travelling alone after dark on highway stretches.",
        hotels=[
            {"name": "The Hosteller Old Manali", "phone": "+91 91376 21270", "distance": "0.3 km from Manu Temple", "rating": 4.6, "tag": "Female dorm available"},
            {"name": "Zostel Manali", "phone": "+91 81308 70008", "distance": "1.2 km from Mall Road", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Mission Hospital Manali", "phone": "+91 1902 252 379", "distance": "2.1 km from hotel"},
            {"name": "Lady Willingdon Hospital", "phone": "+91 1902 252 379", "distance": "3.6 km from hotel"},
        ],
        police=[
            {"name": "Manali Police Station", "phone": "+91 1902 252 326", "distance": "1.4 km from hotel"},
            {"name": "Old Manali Outpost", "phone": "100", "distance": "0.8 km from hotel"},
        ],
        rescue=[
            {"name": "Mountain Rescue Team", "phone": "+91 1902 250 600", "distance": "—"},
            {"name": "HP Tourist Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="udaipur", name="Udaipur", category="Heritage", state="Rajasthan",
        rating=4.6, reviews=188, safety="Very Safe",
        best="Sep - Mar", ideal="Solo, Heritage, Photography",
        budget="₹1,800 - ₹4,500 / day",
        desc="Known as the City of Lakes, Udaipur is a romantic, royal Rajasthani city full of palaces, ghats and rooftop cafes overlooking Lake Pichola.",
        tips="Stay near Lal Ghat or Hanuman Ghat for safe walks at night. Many female-run cafes and homestays in the old city.",
        hotels=[
            {"name": "Zostel Udaipur", "phone": "+91 81308 70008", "distance": "0.2 km from Lake Pichola", "rating": 4.7, "tag": "Female dorm"},
            {"name": "Bunkyard Hostel", "phone": "+91 96604 32100", "distance": "0.4 km from City Palace", "rating": 4.6, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Geetanjali Hospital", "phone": "+91 294 250 0000", "distance": "4.5 km from hotel"},
            {"name": "Paras JK Hospital", "phone": "+91 294 666 0000", "distance": "3.1 km from hotel"},
        ],
        police=[
            {"name": "Ghantaghar Police Station", "phone": "+91 294 252 8001", "distance": "0.7 km from hotel"},
            {"name": "Hathipole Police Station", "phone": "100", "distance": "1.5 km from hotel"},
        ],
        rescue=[
            {"name": "Rajasthan Tourist Police", "phone": "+91 294 241 1535", "distance": "—"},
            {"name": "Women Helpline", "phone": "1091", "distance": "—"},
        ],
    ),
    _d(
        id="ooty", name="Ooty", category="Mountains", state="Tamil Nadu",
        rating=4.5, reviews=210, safety="Very Safe",
        best="Mar - Jun, Sep - Nov", ideal="Solo, Nature, Couples",
        budget="₹1,500 - ₹3,500 / day",
        desc="The Queen of the Nilgiris — Ooty offers misty tea estates, colonial bungalows, the famous toy train and quiet pine forests perfect for slow solo travel.",
        tips="Stay near Charing Cross or Fern Hill. The local toy train and shared cabs are very safe even after sunset.",
        hotels=[
            {"name": "Zostel Plus Ooty", "phone": "+91 81308 70008", "distance": "1.0 km from Botanical Garden", "rating": 4.6, "tag": "Female dorm"},
            {"name": "The Hosteller Ooty", "phone": "+91 91376 21270", "distance": "0.6 km from Charing Cross", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Government Headquarters Hospital", "phone": "+91 423 244 4666", "distance": "1.8 km from hotel"},
            {"name": "ASR Hospital", "phone": "+91 423 244 7575", "distance": "2.3 km from hotel"},
        ],
        police=[
            {"name": "Ooty Town Police Station", "phone": "+91 423 244 3973", "distance": "0.9 km from hotel"},
            {"name": "Charing Cross Outpost", "phone": "100", "distance": "0.4 km from hotel"},
        ],
        rescue=[
            {"name": "Nilgiris Disaster Mgmt", "phone": "+91 423 244 4404", "distance": "—"},
            {"name": "Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="kerala", name="Kerala (Alleppey)", category="Beaches", state="Kerala",
        rating=4.9, reviews=412, safety="Very Safe",
        best="Sep - Mar", ideal="Solo, Couples, Nature",
        budget="₹2,500 - ₹6,000 / day",
        desc="God's Own Country — Alleppey's serene backwaters, houseboats, palm-fringed beaches and Ayurvedic retreats make it a dream solo escape.",
        tips="Choose government-licensed houseboats (DTPC). Stick to public ferries and pre-booked taxis after dark.",
        hotels=[
            {"name": "Zostel Alleppey", "phone": "+91 81308 70008", "distance": "0.5 km from beach", "rating": 4.7, "tag": "Female dorm"},
            {"name": "Bunk Stay Cherai", "phone": "+91 96566 11122", "distance": "0.8 km from backwaters", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "KVM Hospital Cherthala", "phone": "+91 478 281 2222", "distance": "3.5 km from hotel"},
            {"name": "Lourdes Hospital", "phone": "+91 477 226 1234", "distance": "4.2 km from hotel"},
        ],
        police=[
            {"name": "Alappuzha North PS", "phone": "+91 477 225 1100", "distance": "1.0 km from hotel"},
            {"name": "Tourist Police Cell", "phone": "+91 477 226 0796", "distance": "1.6 km from hotel"},
        ],
        rescue=[
            {"name": "Kerala Coastal Police", "phone": "+91 477 224 5300", "distance": "—"},
            {"name": "Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="rishikesh", name="Rishikesh", category="Adventure", state="Uttarakhand",
        rating=4.8, reviews=378, safety="Very Safe",
        best="Sep - Apr", ideal="Solo, Yoga, Adventure",
        budget="₹1,200 - ₹3,500 / day",
        desc="The Yoga Capital of the World on the banks of the Ganga. Rafting, riverside cafes, yoga ashrams and a thriving female solo travel community.",
        tips="Stay near Tapovan or Laxman Jhula. Most ashrams have women-only sections and 10 PM curfews for safety.",
        hotels=[
            {"name": "Zostel Rishikesh", "phone": "+91 81308 70008", "distance": "0.3 km from Laxman Jhula", "rating": 4.7, "tag": "Female dorm"},
            {"name": "Live Free Hostel", "phone": "+91 70177 12345", "distance": "0.5 km from Ganga", "rating": 4.6, "tag": "Female-friendly"},
        ],
        hospitals=[
            {"name": "AIIMS Rishikesh", "phone": "+91 135 246 2901", "distance": "5.6 km from hotel"},
            {"name": "Himalayan Hospital", "phone": "+91 135 247 1133", "distance": "8.2 km from hotel"},
        ],
        police=[
            {"name": "Muni Ki Reti Police Station", "phone": "+91 135 243 1100", "distance": "0.9 km from hotel"},
            {"name": "Rishikesh Kotwali", "phone": "100", "distance": "2.1 km from hotel"},
        ],
        rescue=[
            {"name": "SDRF Rafting Rescue", "phone": "+91 135 244 0083", "distance": "—"},
            {"name": "UK Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="jaipur", name="Jaipur", category="Heritage", state="Rajasthan",
        rating=4.7, reviews=295, safety="Safe",
        best="Oct - Mar", ideal="Solo, Heritage, Shopping",
        budget="₹1,800 - ₹4,500 / day",
        desc="The Pink City — palaces, bazaars, royal forts and Rajasthani colour at every turn. Excellent metro, ride-hailing and tourist police presence.",
        tips="Stay inside the Pink City (near MI Road or Bani Park). Use Ola/Uber instead of unmetered autos at night.",
        hotels=[
            {"name": "Zostel Jaipur", "phone": "+91 81308 70008", "distance": "0.2 km from Hawa Mahal", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Moustache Hostel Jaipur", "phone": "+91 99999 12345", "distance": "1.1 km from City Palace", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Fortis Escorts Jaipur", "phone": "+91 141 254 7000", "distance": "3.2 km from hotel"},
            {"name": "SMS Hospital", "phone": "+91 141 256 0291", "distance": "1.9 km from hotel"},
        ],
        police=[
            {"name": "Manak Chowk Police Station", "phone": "+91 141 261 0163", "distance": "0.5 km from hotel"},
            {"name": "Tourist Police Hawa Mahal", "phone": "+91 141 511 0398", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "Rajasthan Women Helpline", "phone": "1091", "distance": "—"},
            {"name": "Tourist Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="darjeeling", name="Darjeeling", category="Mountains", state="West Bengal",
        rating=4.6, reviews=176, safety="Very Safe",
        best="Mar - May, Oct - Dec", ideal="Solo, Nature, Heritage",
        budget="₹1,500 - ₹3,800 / day",
        desc="Tea gardens, the toy train, sunrise from Tiger Hill and views of Kanchenjunga. Friendly locals and a peaceful pace make it ideal for first-time solo travellers.",
        tips="Stay near Mall Road / Chowrasta. Most homestays are family-run and very welcoming to solo women.",
        hotels=[
            {"name": "The Hosteller Darjeeling", "phone": "+91 91376 21270", "distance": "0.4 km from Mall Road", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Revolver Boutique", "phone": "+91 354 225 8500", "distance": "0.8 km from Chowrasta", "rating": 4.7, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Eden Sadar Hospital", "phone": "+91 354 225 4327", "distance": "1.2 km from hotel"},
            {"name": "Planters' Hospital", "phone": "+91 354 225 4366", "distance": "1.6 km from hotel"},
        ],
        police=[
            {"name": "Sadar Police Station", "phone": "+91 354 225 4422", "distance": "0.8 km from hotel"},
            {"name": "Tourist Police Mall", "phone": "100", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "WB Disaster Mgmt", "phone": "+91 354 225 5749", "distance": "—"},
            {"name": "WB Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="pondicherry", name="Pondicherry", category="Beaches", state="Puducherry",
        rating=4.7, reviews=240, safety="Very Safe",
        best="Oct - Mar", ideal="Solo, Couples, Yoga",
        budget="₹1,800 - ₹4,200 / day",
        desc="Charming French Quarter, sunrise on Promenade Beach, Auroville and quiet bicycle-friendly lanes. One of India's safest tourist cities.",
        tips="Stay in the White Town. Cycles are the safest and most fun way to get around even at night.",
        hotels=[
            {"name": "Zostel Pondicherry", "phone": "+91 81308 70008", "distance": "0.2 km from Promenade", "rating": 4.7, "tag": "Female dorm"},
            {"name": "The Hosteller White Town", "phone": "+91 91376 21270", "distance": "0.4 km from beach", "rating": 4.6, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "JIPMER", "phone": "+91 413 229 6000", "distance": "3.1 km from hotel"},
            {"name": "Aravind Eye Hospital", "phone": "+91 413 261 9100", "distance": "2.4 km from hotel"},
        ],
        police=[
            {"name": "Heritage Town PS", "phone": "+91 413 233 9090", "distance": "0.5 km from hotel"},
            {"name": "Tourist Police White Town", "phone": "100", "distance": "0.2 km from hotel"},
        ],
        rescue=[
            {"name": "Coastal Security Group", "phone": "+91 413 222 6789", "distance": "—"},
            {"name": "Tourist Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="shimla", name="Shimla", category="Mountains", state="Himachal Pradesh",
        rating=4.5, reviews=205, safety="Very Safe",
        best="Mar - Jun, Dec - Feb", ideal="Solo, Snow, Heritage",
        budget="₹1,600 - ₹3,800 / day",
        desc="The colonial Queen of Hills with toy train rides, snow in winter, ridge walks and the iconic Mall Road. Very tourist-friendly.",
        tips="Mall Road and The Ridge are pedestrian-only and well-policed. Avoid the lower bazaar after 10 PM.",
        hotels=[
            {"name": "Zostel Shimla", "phone": "+91 81308 70008", "distance": "0.3 km from Mall Road", "rating": 4.6, "tag": "Female dorm"},
            {"name": "The Hosteller Shimla", "phone": "+91 91376 21270", "distance": "0.7 km from Ridge", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "IGMC Shimla", "phone": "+91 177 280 4251", "distance": "1.6 km from hotel"},
            {"name": "DDU Hospital", "phone": "+91 177 265 4713", "distance": "0.9 km from hotel"},
        ],
        police=[
            {"name": "Sadar Police Station", "phone": "+91 177 265 6535", "distance": "0.4 km from hotel"},
            {"name": "Mall Road Tourist Police", "phone": "100", "distance": "0.2 km from hotel"},
        ],
        rescue=[
            {"name": "HP Disaster Mgmt", "phone": "+91 177 262 8940", "distance": "—"},
            {"name": "HP Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="munnar", name="Munnar", category="Mountains", state="Kerala",
        rating=4.7, reviews=260, safety="Very Safe",
        best="Sep - Mar", ideal="Solo, Couples, Nature",
        budget="₹1,800 - ₹4,500 / day",
        desc="Endless rolling tea plantations, misty viewpoints and quiet jungle trails. Munnar is the kind of green silence solo travellers crave.",
        tips="Stay near Munnar town and book guided plantation walks. Avoid travelling on hill roads after dark.",
        hotels=[
            {"name": "Zostel Munnar", "phone": "+91 81308 70008", "distance": "1.1 km from town", "rating": 4.6, "tag": "Female dorm"},
            {"name": "The Hosteller Munnar", "phone": "+91 91376 21270", "distance": "0.9 km from tea museum", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Tata General Hospital", "phone": "+91 4865 230 270", "distance": "2.3 km from hotel"},
            {"name": "St. John's Hospital Kattappana", "phone": "+91 4868 250 240", "distance": "32 km from hotel"},
        ],
        police=[
            {"name": "Munnar Police Station", "phone": "+91 4865 230 333", "distance": "1.0 km from hotel"},
            {"name": "Devikulam PS", "phone": "100", "distance": "6.8 km from hotel"},
        ],
        rescue=[
            {"name": "Forest Rescue Munnar", "phone": "+91 4865 231 587", "distance": "—"},
            {"name": "Kerala Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="coorg", name="Coorg", category="Mountains", state="Karnataka",
        rating=4.6, reviews=230, safety="Very Safe",
        best="Oct - Mar", ideal="Solo, Couples, Nature",
        budget="₹1,800 - ₹4,000 / day",
        desc="Coffee estates, waterfalls and misty mornings — Coorg (Kodagu) is a peaceful retreat with a strong network of family-run homestays.",
        tips="Pick estate homestays around Madikeri. Carry layers; evenings get chilly even in summer.",
        hotels=[
            {"name": "Zostel Coorg", "phone": "+91 81308 70008", "distance": "1.4 km from Madikeri", "rating": 4.6, "tag": "Female dorm"},
            {"name": "The Hosteller Coorg", "phone": "+91 91376 21270", "distance": "0.8 km from Raja's Seat", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "District Hospital Madikeri", "phone": "+91 8272 222 770", "distance": "1.5 km from hotel"},
            {"name": "Karuna Hospital", "phone": "+91 8272 228 880", "distance": "2.1 km from hotel"},
        ],
        police=[
            {"name": "Madikeri Town PS", "phone": "+91 8272 225 207", "distance": "0.7 km from hotel"},
            {"name": "Tourist Police", "phone": "100", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "Kodagu Disaster Mgmt", "phone": "+91 8272 221 077", "distance": "—"},
            {"name": "KA Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="hampi", name="Hampi", category="Heritage", state="Karnataka",
        rating=4.6, reviews=185, safety="Safe",
        best="Oct - Feb", ideal="Solo, Heritage, Photography",
        budget="₹1,200 - ₹3,000 / day",
        desc="A UNESCO ruins-scape of boulders, temples and ancient bazaars. Hampi is otherworldly and wildly photogenic — perfect for slow solo travel.",
        tips="Stay on the Hampi Bazaar side for safety; cross to Virupapur Gadde only during day. Cycles are the best way around.",
        hotels=[
            {"name": "Zostel Hampi", "phone": "+91 81308 70008", "distance": "0.3 km from Hampi Bazaar", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Padma Guesthouse", "phone": "+91 8394 241 331", "distance": "0.5 km from Virupaksha Temple", "rating": 4.4, "tag": "Female-friendly homestay"},
        ],
        hospitals=[
            {"name": "Hampi PHC", "phone": "+91 8394 241 222", "distance": "1.2 km from hotel"},
            {"name": "Hospet Govt Hospital", "phone": "+91 8394 228 230", "distance": "12 km from hotel"},
        ],
        police=[
            {"name": "Hampi Police Station", "phone": "+91 8394 241 241", "distance": "0.6 km from hotel"},
            {"name": "Tourist Police Hampi", "phone": "100", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "ASI Heritage Helpline", "phone": "+91 8394 241 339", "distance": "—"},
            {"name": "KA Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="pushkar", name="Pushkar", category="Heritage", state="Rajasthan",
        rating=4.5, reviews=158, safety="Safe",
        best="Oct - Mar", ideal="Solo, Spiritual, Backpackers",
        budget="₹1,200 - ₹3,000 / day",
        desc="Holy lake, ghats, the famous camel fair and dozens of rooftop cafes. Pushkar is small, walkable and full of friendly backpackers.",
        tips="Respect the dress code at the lake (covered shoulders + legs). Beware of fake 'priests' offering blessings on the ghats.",
        hotels=[
            {"name": "Zostel Pushkar", "phone": "+91 81308 70008", "distance": "0.2 km from Brahma Temple", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Moustache Hostel Pushkar", "phone": "+91 99999 12345", "distance": "0.5 km from Pushkar Lake", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Govt Hospital Pushkar", "phone": "+91 145 277 2025", "distance": "1.0 km from hotel"},
            {"name": "JLN Hospital Ajmer", "phone": "+91 145 242 9613", "distance": "14 km from hotel"},
        ],
        police=[
            {"name": "Pushkar Police Station", "phone": "+91 145 277 2032", "distance": "0.5 km from hotel"},
            {"name": "Tourist Police", "phone": "100", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "Rajasthan Tourist Helpline", "phone": "1363", "distance": "—"},
            {"name": "Women Helpline", "phone": "1091", "distance": "—"},
        ],
    ),
    _d(
        id="varanasi", name="Varanasi", category="Heritage", state="Uttar Pradesh",
        rating=4.5, reviews=215, safety="Safe",
        best="Oct - Mar", ideal="Solo, Spiritual, Photography",
        budget="₹1,200 - ₹3,000 / day",
        desc="The spiritual capital of India — Ganga aarti, ghats, ancient temples and a unique soul that every solo traveller writes home about.",
        tips="Stay at Assi Ghat or Dashashwamedh Ghat. Boat rides at sunrise are safest; avoid the inner alleys at night.",
        hotels=[
            {"name": "Zostel Varanasi", "phone": "+91 81308 70008", "distance": "0.3 km from Assi Ghat", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Moustache Varanasi", "phone": "+91 99999 12345", "distance": "0.4 km from Dashashwamedh Ghat", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "BHU Sir Sundarlal Hospital", "phone": "+91 542 236 9528", "distance": "3.0 km from hotel"},
            {"name": "Heritage Hospitals", "phone": "+91 542 250 8000", "distance": "4.5 km from hotel"},
        ],
        police=[
            {"name": "Bhelupur Police Station", "phone": "+91 542 227 7400", "distance": "0.9 km from hotel"},
            {"name": "Dashashwamedh Outpost", "phone": "100", "distance": "0.3 km from hotel"},
        ],
        rescue=[
            {"name": "NDRF River Rescue", "phone": "+91 542 250 8484", "distance": "—"},
            {"name": "UP Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="andamans", name="Andaman Islands", category="Beaches", state="Andaman & Nicobar",
        rating=4.9, reviews=320, safety="Very Safe",
        best="Oct - May", ideal="Solo, Diving, Beaches",
        budget="₹3,000 - ₹7,000 / day",
        desc="Crystal-clear water, white sand and coral reefs. Havelock and Neil Island are calm, safe and full of solo female divers and backpackers.",
        tips="Stay in Havelock for the safest beach scene. Pre-book inter-island ferries to avoid last-minute hassles.",
        hotels=[
            {"name": "Zostel Havelock", "phone": "+91 81308 70008", "distance": "0.6 km from Vijaynagar Beach", "rating": 4.7, "tag": "Female dorm"},
            {"name": "Pellicano Resort", "phone": "+91 3192 282 222", "distance": "0.4 km from beach 5", "rating": 4.6, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "GB Pant Hospital Port Blair", "phone": "+91 3192 232 102", "distance": "Inter-island"},
            {"name": "Havelock CHC", "phone": "+91 3192 282 102", "distance": "1.5 km from hotel"},
        ],
        police=[
            {"name": "Havelock Police Station", "phone": "+91 3192 282 100", "distance": "0.8 km from hotel"},
            {"name": "Port Blair Tourist Police", "phone": "100", "distance": "Inter-island"},
        ],
        rescue=[
            {"name": "Indian Coast Guard", "phone": "1554", "distance": "—"},
            {"name": "A&N Tourism Helpline", "phone": "1363", "distance": "—"},
        ],
    ),
    _d(
        id="spiti", name="Spiti Valley", category="Adventure", state="Himachal Pradesh",
        rating=4.8, reviews=140, safety="Safe",
        best="May - Oct", ideal="Solo, Adventure, Photography",
        budget="₹2,000 - ₹4,500 / day",
        desc="A high-altitude cold desert of monasteries, fossil villages and Mars-like landscapes. A bucket-list trip for adventurous solo travellers.",
        tips="Acclimatise in Kaza for 2 days before going higher. Carry cash — ATMs are few. Travel only with verified drivers.",
        hotels=[
            {"name": "Zostel Spiti (Kaza)", "phone": "+91 81308 70008", "distance": "0.3 km from Kaza Bazaar", "rating": 4.7, "tag": "Female dorm"},
            {"name": "Sakya Abode Homestay", "phone": "+91 1906 222 256", "distance": "0.5 km from monastery", "rating": 4.6, "tag": "Female-friendly"},
        ],
        hospitals=[
            {"name": "Kaza Civil Hospital", "phone": "+91 1906 222 232", "distance": "0.6 km from hotel"},
            {"name": "Reckong Peo Hospital", "phone": "+91 1786 222 224", "distance": "210 km from hotel"},
        ],
        police=[
            {"name": "Kaza Police Station", "phone": "+91 1906 222 235", "distance": "0.4 km from hotel"},
            {"name": "Tabo Outpost", "phone": "100", "distance": "47 km from hotel"},
        ],
        rescue=[
            {"name": "ITBP Mountain Rescue", "phone": "+91 1906 222 222", "distance": "—"},
            {"name": "HP Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="kasol", name="Kasol", category="Mountains", state="Himachal Pradesh",
        rating=4.6, reviews=195, safety="Safe",
        best="Mar - Jun, Sep - Nov", ideal="Solo, Backpackers, Trekking",
        budget="₹1,200 - ₹3,000 / day",
        desc="Mini Israel of India — pine forests, the Parvati river, Israeli cafes and Kheerganga treks. A backpacker classic with a friendly hostel scene.",
        tips="Stay in main Kasol or Chalal. Avoid solo treks beyond Kheerganga without a registered guide.",
        hotels=[
            {"name": "The Hosteller Kasol", "phone": "+91 91376 21270", "distance": "0.2 km from Parvati river", "rating": 4.6, "tag": "Female dorm"},
            {"name": "Zostel Kasol", "phone": "+91 81308 70008", "distance": "0.4 km from Kasol bus stand", "rating": 4.5, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Kasol Civil Hospital", "phone": "+91 1902 273 015", "distance": "0.7 km from hotel"},
            {"name": "Kullu Regional Hospital", "phone": "+91 1902 222 223", "distance": "32 km from hotel"},
        ],
        police=[
            {"name": "Kasol Police Outpost", "phone": "+91 1902 273 030", "distance": "0.5 km from hotel"},
            {"name": "Manikaran PS", "phone": "100", "distance": "5 km from hotel"},
        ],
        rescue=[
            {"name": "SDRF Parvati Valley", "phone": "+91 1902 222 100", "distance": "—"},
            {"name": "HP Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="mussoorie", name="Mussoorie", category="Mountains", state="Uttarakhand",
        rating=4.5, reviews=180, safety="Very Safe",
        best="Mar - Jun, Sep - Nov", ideal="Solo, Couples, Family",
        budget="₹1,800 - ₹4,000 / day",
        desc="The Queen of the Hills — a charming colonial-era hill station with the famous Camel's Back Road, Kempty Falls and panoramic Doon Valley views.",
        tips="The Mall Road is pedestrian-only after sunset and very safe. Avoid private taxis after 10 PM.",
        hotels=[
            {"name": "Zostel Mussoorie", "phone": "+91 81308 70008", "distance": "0.4 km from Mall Road", "rating": 4.6, "tag": "Female dorm"},
            {"name": "The Hosteller Landour", "phone": "+91 91376 21270", "distance": "1.2 km from Char Dukan", "rating": 4.6, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Mussoorie Civil Hospital", "phone": "+91 135 263 2444", "distance": "1.0 km from hotel"},
            {"name": "Landour Community Hospital", "phone": "+91 135 263 2541", "distance": "2.4 km from hotel"},
        ],
        police=[
            {"name": "Mussoorie Police Station", "phone": "+91 135 263 2999", "distance": "0.6 km from hotel"},
            {"name": "Tourist Police Mall Road", "phone": "100", "distance": "0.2 km from hotel"},
        ],
        rescue=[
            {"name": "SDRF Garhwal", "phone": "+91 135 271 6202", "distance": "—"},
            {"name": "UK Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
    _d(
        id="mcleodganj", name="McLeod Ganj", category="Mountains", state="Himachal Pradesh",
        rating=4.7, reviews=205, safety="Very Safe",
        best="Mar - Jun, Sep - Nov", ideal="Solo, Spiritual, Trekking",
        budget="₹1,200 - ₹3,200 / day",
        desc="The home of the Dalai Lama, with Tibetan monasteries, prayer flags, momos and the legendary Triund trek. One of India's safest hill towns for solo women.",
        tips="Stay near the main square or Bhagsu. Volunteer with local NGOs for an immersive, community-rooted experience.",
        hotels=[
            {"name": "Zostel McLeodGanj", "phone": "+91 81308 70008", "distance": "0.3 km from main square", "rating": 4.7, "tag": "Female dorm"},
            {"name": "The Hosteller McLeod", "phone": "+91 91376 21270", "distance": "0.6 km from Tsuglagkhang", "rating": 4.6, "tag": "Solo-friendly"},
        ],
        hospitals=[
            {"name": "Delek Hospital", "phone": "+91 1892 222 053", "distance": "0.9 km from hotel"},
            {"name": "Zonal Hospital Dharamshala", "phone": "+91 1892 224 050", "distance": "8.5 km from hotel"},
        ],
        police=[
            {"name": "McLeod Ganj Police Station", "phone": "+91 1892 221 483", "distance": "0.4 km from hotel"},
            {"name": "Tourist Police Bhagsu", "phone": "100", "distance": "1.1 km from hotel"},
        ],
        rescue=[
            {"name": "Dhauladhar Rescue Team", "phone": "+91 1892 222 100", "distance": "—"},
            {"name": "HP Tourism Helpline", "phone": "1364", "distance": "—"},
        ],
    ),
]
