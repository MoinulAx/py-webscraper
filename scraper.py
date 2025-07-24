import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class EventScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)

    def login(self, login_url: str):
        self.driver.get(login_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)

    def scrape_events(self, events_page_url: str):
        self.driver.get(events_page_url)
        time.sleep(3)

        events = []
        event_elements = self.driver.find_elements(By.CLASS_NAME, "event-card")

        for event in event_elements:
            try:
                title = event.find_element(By.CLASS_NAME, "event-title").text
                date = event.find_element(By.CLASS_NAME, "event-date").text
                time_ = event.find_element(By.CLASS_NAME, "event-time").text
                link = event.find_element(By.TAG_NAME, "a").get_attribute("href")
                description = event.find_element(By.CLASS_NAME, "event-description").text

                events.append({
                    "title": title,
                    "date": date,
                    "time": time_,
                    "link": link,
                    "description": description,
                })
            except Exception as e:
                print("Error extracting event:", e)

        return events

    def close(self):
        self.driver.quit()
