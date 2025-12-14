from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
from backend.routers import api
from backend.services.scraper_service import scraper_service
from backend.services.storage_service import storage_service
from backend.core.config import CITY_CONFIG
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Pharmora")

# Scheduler Task
def daily_scrape_job():
    logger.info("Starting Daily Scrape Job...")
    for city in CITY_CONFIG.keys():
        try:
            logger.info(f"Scraping {city}...")
            data = scraper_service.scrape_city(city)
            storage_service.save_data(city, data)
        except Exception as e:
            logger.error(f"Failed to scrape {city}: {e}")
    logger.info("Daily Scrape Job Completed.")

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start Scheduler
    scheduler = BackgroundScheduler()
    # Runs everyday at 00:30 as requested
    scheduler.add_job(daily_scrape_job, 'cron', hour=0, minute=30)
    # Also run once on startup for Demo purposes (since Render sleeps)
    scheduler.add_job(daily_scrape_job, 'date') 
    scheduler.start()
    
    yield
    
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(api.router)

@app.get("/")
def health_check():
    return {"status": "Pharmora API Running", "mode": "Ethical Scraper"}
