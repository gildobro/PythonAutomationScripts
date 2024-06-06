from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime



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
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def write_file(text):
    """Write input text into a text file"""
    #Current time
    current_time = datetime.datetime.now()

    filename = current_time.strftime("%Y-%m-%d.%H-%M-%S") + ".txt"
    with open(filename, 'w') as file:
        file.write(text)
        
    # print(f"File created: {filename}")



def main():
    driver = get_driver()
    #Log In
    driver.find_element(By.ID, "id_username").send_keys("automated")
    #Input password and press Enter
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)

    #Click Home Button
    driver.find_element(By.CLASS_NAME, "navbar-brand").click()

    while True:
        time.sleep(2)
        #Scrape Text
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)



print(main())
