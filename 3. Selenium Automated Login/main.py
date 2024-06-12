from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    #input username
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    #Input password and press Enter
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)

    #Click on the Sign in Button
    #driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/form/button").click()

    #Clieck on the home button
    driver.find_element(By.CLASS_NAME, "navbar-brand").click()
    time.sleep(2)

    #Scrape home page text quote
    #element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    time.sleep(2)

    print("The average world temperature is: ", clean_text(element.text))


print(main())