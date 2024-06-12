from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#Initialize Driver
def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


def main():
    driver = get_driver()

    #Login Fillout
    driver.find_element(By.ID, "CustomerEmail").send_keys("gdobrovinsky@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "CustomerPassword").send_keys("test12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/article/section/div/div[1]/form/button").click()
    time.sleep(2)

    #Navigate to the contact us page
    driver.find_element(By.XPATH, "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    print(driver.current_url)


print(main())