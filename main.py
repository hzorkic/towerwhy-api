from fastapi import FastAPI
from scraper import Scraper
from datetime import datetime

app = FastAPI()
lit = Scraper()

@app.get('/{cat}')

async def read_item(cat):

    # Replace with actual date input
    #today_date_str = "2024-06-30"
    today_date = datetime.strptime(cat, "%Y-%m-%d").date()

    # Fetch today's event description
    return Scraper.fetch_today_event(today_date)


