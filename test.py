from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_eventbrite_selenium(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-event-id]"))
        )
    except:
        print("Event cards did not load.")
        driver.quit()
        return []

    html = driver.page_source

    # Optional: save the page for debugging
    with open("eventbrite.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select("[data-event-id]")

    events = []
    for card in cards:
        title_tag = card.select_one("a.eds-event-card-content__action-link")
        date_tag = card.select_one("div.eds-event-card-content__sub-content div.eds-text-bs")

        title = title_tag.get_text(strip=True) if title_tag else None
        link = urljoin(url, title_tag["href"]) if title_tag and title_tag.has_attr("href") else None
        date = date_tag.get_text(strip=True) if date_tag else None

        if title and date:
            events.append({
                "title": title,
                "date_time": date,
                "link": link
            })

    driver.quit()

    print(f"Found {len(events)} events")
    return events

if __name__ == "__main__":
    url = "https://www.eventbrite.com/d/ny--new-york/events/"
    data = scrape_eventbrite_selenium(url)
    for e in data[:5]:
        print(e)
