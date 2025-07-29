from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class EventScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def login(self, login_url: str, email: str, password: str):
        self.driver.get(login_url)
        time.sleep(2)

        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(3)

    def scrape_events(self, events_url: str):
        self.driver.get(events_url)
        time.sleep(2)

        events = []
        event_elements = self.driver.find_elements(By.CLASS_NAME, "event-card")  # You’ll update this

        for e in event_elements:
            try:
                title = e.find_element(By.CLASS_NAME, "event-title").text
                date = e.find_element(By.CLASS_NAME, "event-date").text
                time_ = e.find_element(By.CLASS_NAME, "event-time").text
                link = e.find_element(By.TAG_NAME, "a").get_attribute("href")
                about = e.find_element(By.CLASS_NAME, "event-description").text

                events.append({
                    "title": title,
                    "date": date,
                    "time": time_,
                    "link": link,
                    "about": about,
                })
            except Exception:
                continue

        return events

    def close(self):
        self.driver.quit()
