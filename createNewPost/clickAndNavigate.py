import datetime
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

def scrollAndClick(browser, element):
    browser.execute_script("arguments[0].scrollIntoView();", element)
    browser.execute_script("window.scrollBy(0, -200)","")
    click(element)


def click(element):
    element_is_interactable = False
    startTime = datetime.datetime.now()
    counter = 1

    if element:
        while not element_is_interactable and not (datetime.datetime.now() - startTime > datetime.timedelta(seconds=100)):
            try:
                element.click()
                element_is_interactable = True
            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException) as e:
                counter += 1
    sleep(2)  
    return element_is_interactable

def waitToClick(browser, method, methodValue):
    element = ""
    for i in range(0, 100):
        try:
            if method == "XPATH":
                element = browser.find_element(By.XPATH, methodValue)
                element.click()
                
            elif method == "CLASS_NAME":
                element = browser.find_element(By.CLASS_NAME, methodValue)
                element.click()
            elif method == "ID":
                element = browser.find_element(By.ID, methodValue)
                element.click()
            elif method == "LINK_TEXT":
                element = browser.find_element(By.LINK_TEXT, methodValue)
                element.click()
            return element
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            sleep(0.2)
            continue