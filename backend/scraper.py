import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from models import Pharmacy
from mock_data import generate_mock_data
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_pharmacies(city: str, district: Optional[str] = None) -> List[Pharmacy]:
    results = []
    
    # 1. Try eczaneler.gen.tr (Often blocked but worth a shot)
    try:
        url = f"https://www.eczaneler.gen.tr/nobetci-{city}"
        if district:
            url += f"-{district}"
            
        print(f"Scraping: {url}")
        response = requests.get(url, headers=HEADERS, timeout=5)
        
        if response.status_code == 200 and "Cloudflare" not in response.text:
            soup = BeautifulSoup(response.content, 'lxml')
            cards = soup.select('div.col-lg-3.col-md-6') 
            
            for card in cards:
                try:
                    name = card.select_one('.card-header .h5').get_text(strip=True)
                    body = card.select_one('.card-body')
                    address = body.select_one('address').get_text(" ", strip=True)
                    phone_el = body.select_one('a[href^="tel:"]')
                    phone = phone_el.get_text(strip=True) if phone_el else ""
                    
                    # Coords
                    map_link = body.select_one('a[href*="maps.google.com"]')
                    lat, lng = None, None
                    if map_link:
                        href = map_link.get('href')
                        if 'q=' in href:
                            coords = href.split('q=')[1].split(',')
                            lat = float(coords[0])
                            lng = float(coords[1].split('&')[0])

                    results.append(Pharmacy(
                        name=name,
                        district=district or city,
                        neighborhood="",
                        address=address,
                        phone=phone,
                        lat=lat,
                        lng=lng
                    ))
                except:
                    continue
                    
        if results:
            return results

    except Exception as e:
        print(f"Scrape failed: {e}")

    # 2. Fallback to Mock Data if scraping failed or returned 0
    print("Scraping failed or blocked. Using Mock Data.")
    mock_raw = generate_mock_data(city, district)
    
    for m in mock_raw:
        results.append(Pharmacy(**m))
        
    return results
