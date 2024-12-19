from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

from clickAndNavigate import click

def uploadFiles(browser, files, websiteGen, downloads, filesExist):

    if (filesExist == False):
        return

    logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

    if (len(files) == 0): #Checking if there are any files to upload
        return
    
    filePaths = []
    totalFileSize = 0

    #Creating multiple lists of file paths to upload each not exceeding 16MB
    for i in range(len(files)):
        if files[i]["fileName"].endswith(".zip"):
            print("Datoteka" + '"' + files[i]["fileName"] + '"' + " je u '.zip' formatu. Morate je uploadati ručno.\n")
            continue

        if files[i]["kbSize"] > 16000: #Checking if the file size is less than 16MB
            print("Datoteka" + '"' + files[i]["fileName"] + '"' + " je prevelika za upload. Morate je uploadati ručno.\n")
            continue

        if (files[i]["kbSize"] + totalFileSize) < 16000: #Checking if the total size of the files is less than 16MB
            filePaths.append(downloads + '\\' + files[i]["fileName"])
            totalFileSize += files[i]["kbSize"]
  
        try:
            if (files[i+1]["kbSize"] + totalFileSize >= 16000) or len(filePaths) == 20: #Uploading files if the total size of the files + the size of the current file is would be more than 16MB or if it's the last file
                browser.execute_script("arguments[0].scrollIntoView();", logo)
                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button

                for i in range(100):
                    try:
                        browser.find_element(By.ID, "upload-file").send_keys('\n'.join(filePaths)) ##Getting the input button and uploading the images
                        break
                    except NoSuchElementException or ElementNotInteractableException:
                        sleep(0.1)  

                logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

                browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

                click(browser.find_element(By.XPATH, "//button[text()=' Start Upload']")) #Clicking the start upload button

                filePaths = []
                totalFileSize = 0
                continue
        except IndexError:
            continue

    #Uploading left over files    
    if (len(filePaths) > 0):
        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes
        browser.execute_script("arguments[0].scrollIntoView();", logo)
        browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button

        browser.find_element(By.ID, "upload-file").send_keys('\n'.join(filePaths)) ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        click(browser.find_element(By.XPATH, "//button[text()=' Start Upload']")) #Clicking the start upload button
            
    #sleep(5)
