from scraper import EventScraper
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    events_url = os.getenv("EVENTS_PAGE_URL")

    scraper = EventScraper()
    events = scraper.scrape_events(events_url)

    for event in events:
        print(event)

    scraper.close()
