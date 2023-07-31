from selenium.webdriver.common.by import By
from time import sleep

from clickAndNavigate import click

def uploadFiles(browser, files, websiteGen, downloads):
    filesExist = False
    print(files)
    logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

    if (len(files) == 0): #Checking if there are any files to upload
        return
    
    filePaths = []

    for file in files:
        filePaths.append(downloads + '\\' + file["fileName"])

    print(filePaths)

    browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button

    browser.find_element(By.ID, "upload-file").send_keys('\n'.join(filePaths)) ##Getting the input button and uploading the images

    logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

    browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

    click(browser.find_element(By.XPATH, "//button[text()=' Start Upload']")) #Clicking the start upload button
    
    filesExist = True

    sleep(5)
   
    return filesExist