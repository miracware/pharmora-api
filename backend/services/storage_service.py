import json
import os
import datetime
from backend.core.config import CACHE_FILE
import logging

logger = logging.getLogger(__name__)

class StorageService:
    def __init__(self):
        # Ensure dir exists
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        if not os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump({"updated_at": None, "data": {}}, f)

    def get_data(self, city):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_data = data.get("data", {}).get(city)
            # You could add expiration logic here (24h)
            return city_data
        except Exception as e:
            logger.error(f"Cache read error: {e}")
            return None

    def save_data(self, city, pharmacies):
        try:
            # Read existing
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                full_data = json.load(f)
            
            # Update
            full_data["data"][city] = pharmacies
            full_data["updated_at"] = datetime.datetime.now().isoformat()
            
            # Write back
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(full_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Cache write error: {e}")

storage_service = StorageService()
