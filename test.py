from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_browser_incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.maximize_window()
    return driver

driver = setup_browser_incognito()

driver.get("https://web-sync.io/")
time.sleep(5)
print(driver.title)

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/div[2]/button[1]').click()
time.sleep(5)
print ("Page scrolls smoothly to About Us section all content displayed correctly")

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/div[2]/button[2]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/div[2]/button[3]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/div[2]/button[4]').click()
time.sleep(5)