import json
import os

# Risk Levels
RISK_LOW = "LOW"
RISK_MEDIUM = "MEDIUM"
RISK_HIGH = "HIGH"

# Default Configuration based on the tutorial's risk assessment
CITY_CONFIG = {
    "istanbul": {"risk": RISK_HIGH, "plate": 34},
    "ankara": {"risk": RISK_HIGH, "plate": 6},
    "izmir": {"risk": RISK_HIGH, "plate": 35},
    "bursa": {"risk": RISK_HIGH, "plate": 16},
    "antalya": {"risk": RISK_HIGH, "plate": 7},
    "sanliurfa": {"risk": RISK_MEDIUM, "plate": 63},
    "gaziantep": {"risk": RISK_HIGH, "plate": 27},
    "adana": {"risk": RISK_HIGH, "plate": 1},
    # Add more as needed or load from a full JSON
}

# Generic User Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "NobetciEczaneBot/1.0 (Ethical Scraper; +https://pharmora.app)"
]

CACHE_FILE = os.path.join(os.path.dirname(__file__), "../data/pharmacy_cache.json")
