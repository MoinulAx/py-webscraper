from scraper import EventScraper
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    login_url = os.getenv("LOGIN_URL")
    events_url = os.getenv("EVENTS_PAGE_URL")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    scraper = EventScraper()
    scraper.login(login_url, email, password)
    events = scraper.scrape_events(events_url)

    for event in events:
        print(event)

    scraper.close()
