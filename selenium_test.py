# selenium_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time


os.makedirs("logs", exist_ok=True)
log_file = open("logs/selenium_log.txt", "w")

def log(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    log_file.write(f"{timestamp} {message}\n")
    log_file.flush()  # flush immediately

driver = webdriver.Chrome()  

try:
    log("[TEST] Starting test: test_google_search")
    driver.get("https://www.google.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("ERS Embedded Systems\n")
    time.sleep(2)

    log("[PASS] test_google_search completed successfully")

except NoSuchElementException as e:
    log("[ERROR] Element not found: " + str(e))
    log("[FAIL] test_google_search failed")

finally:
    driver.quit()
    log_file.close()
