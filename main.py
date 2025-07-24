from scraper import EventScraper

if __name__ == "__main__":
    login_url = "https://example.com/login"  # replace with actual login URL
    events_page_url = "https://example.com/events"  # replace with actual events page

    scraper = EventScraper()
    scraper.login(login_url)
    events = scraper.scrape_events(events_page_url)

    for event in events:
        print(event)

    scraper.close()
