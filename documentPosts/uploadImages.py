from selenium.webdriver.common.by import By
from navToFolder import createFolderAndNavigate
from os.path import exists

from clickAndNavigate import click

def uploadImages(browser, imgFile, downloads, imageNum, folder, websiteGen):
    naslovnaExists = False
    albumExists = False

    logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

    #Uploading the naslovna.jpg file
    if (exists(downloads + '\\' + "naslovna.jpg")): #Check if the naslovna.jpg file exists in the downloads folder
        browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it

        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "naslovna.jpg") ##Getting the input button and uploading the images

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        browser.find_element(By.XPATH, "//button[text()=' Start Upload']").click() #Clicking the start upload button

        naslovnaExists = True
    elif (exists(imgFile + '\\' + "naslovna.jpg")):
        browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it

        browser.find_element(By.ID, "upload-file").send_keys(imgFile + '\\' + "naslovna.jpg") ##Getting the input button and uploading the images

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        browser.find_element(By.XPATH, "//button[text()=' Start Upload']").click() #Clicking the start upload button

        naslovnaExists = True

    #Uploading the images from "Album"
    if (exists(imgFile) and imageNum > 0):

        albumFolder = folder + "-" + "album" #Getting the album folder

        createFolderAndNavigate(browser, "album", albumFolder)

        filePaths = []

        #Creating a list of file paths
        for i in range(1, imageNum + 1):
            filePaths.append(imgFile + '\\' + str(i).rjust(2, '0') + ".jpg")

        browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button

        browser.find_element(By.ID, "upload-file").send_keys('\n'.join(filePaths)) ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        click(browser.find_element(By.XPATH, "//button[text()=' Start Upload']")) #Clicking the start upload button

        albumExists = True

    return naslovnaExists, albumExists