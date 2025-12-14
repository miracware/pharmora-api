from datetime import datetime
import random

def generate_mock_data(city, district):
    """Fallback generator when scraping is blocked"""
    districts = [district] if district else ['Merkez', 'Kadikoy', 'Besiktas', 'Cankaya', 'Konak']
    pharmacies = []
    
    # Realistic sounding names
    names = ["Hayat", "Sifa", "Anadolu", "Yeni", "Merkez", "Deva", "Ege", "Akdeniz", "Gunes", "Yildiz"]
    
    for i in range(5):
        d = random.choice(districts)
        name = f"{random.choice(names)} Eczanesi"
        
        # Approximate coords (Turkey center-ish or city specific if we had a db)
        # Random offset from a base
        base_lat, base_lng = 41.0082, 28.9784 # Istanbul
        if city.lower() == 'ankara': base_lat, base_lng = 39.9334, 32.8597
        if city.lower() == 'izmir': base_lat, base_lng = 38.4192, 27.1287
        
        lat = base_lat + random.uniform(-0.05, 0.05)
        lng = base_lng + random.uniform(-0.05, 0.05)
        
        pharmacies.append({
            "name": name,
            "district": d.capitalize(),
            "neighborhood": f"{d.capitalize()} Mah.",
            "address": f"{d.capitalize()} Cad. No:{random.randint(1,100)} {city.capitalize()}",
            "phone": f"0(212) {random.randint(200,999)} {random.randint(10,99)} {random.randint(10,99)}",
            "lat": lat,
            "lng": lng
        })
    return pharmacies
