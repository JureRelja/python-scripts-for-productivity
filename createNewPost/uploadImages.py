from selenium.webdriver.common.by import By
from navToFolder import createFolderAndNavigate
from os.path import exists
import math
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from time import sleep

from clickAndNavigate import click
from clickAndNavigate import scrollAndClick
from clickAndNavigate import scrollAndClick
from resize import removeFiles

def uploadImages(browser, imgFile, downloads, imageNum, secondAlbumType, folder, websiteGen):
    naslovnaExists = False
    albumExists = False

    logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

    browser.execute_script("arguments[0].scrollIntoView();", logo)

    #Uploading the naslovna.jpg file
    if (exists(downloads + '\\' + "naslovna.jpg")): #Check if the naslovna.jpg file exists in the downloads folder
        
        for i in range(10):
            try: 
                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);
        
        for i in range(100):
            try:
                browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "naslovna.jpg") ##Getting the input button and uploading the images
                break
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)  
            
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible
        
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']")
                click(element) #cicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)
        
        naslovnaExists = True
    elif (exists(imgFile + '\\' + "naslovna.jpg")):
        for i in range(10):
            try: 
                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);
                #clicking start upload button

        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "naslovna.jpg") ##Getting the input button and uploading the images

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']")
                element.click() #Clicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)

        naslovnaExists = True

    if (secondAlbumType == "two_albums"):
        albumFolder = folder + "-" + "album" #Getting the album folder

        createFolderAndNavigate(browser, "album", albumFolder)   

        for i in range(10):
            try:    

                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);
        
        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "1.jpg") ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        #clicking start upload button
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']")
                element.click() #Clicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)
        
        for i in range(100):
            try: 
                oldfolder = browser.find_element(By.ID, folder).find_element(By.XPATH, "*") #Getting the newly created folder for the current year
                scrollAndClick(browser, oldfolder)
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.5)

        albumFolder = folder + "-" + "album2" #Getting the album folder

        createFolderAndNavigate(browser, "album2", albumFolder)      

        browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it

        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "2.jpg") ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        #clicking start upload button
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']") 
                element.click() #Clicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)

        albumExists = True

    if (secondAlbumType == "main_img_album_and_galery"):
        albumFolder = folder + "-" + "album" #Getting the album folder

        createFolderAndNavigate(browser, "album", albumFolder)   

        for i in range(10):
            try:    

                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);
        
        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "1.jpg") ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        #clicking start upload button
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']")
                element.click() #Clicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)
        
        for i in range(100):
            try: 
                oldfolder = browser.find_element(By.ID, folder).find_element(By.XPATH, "*") #Getting the newly created folder for the current year
                scrollAndClick(browser, oldfolder)
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.5)

        albumFolder = folder + "-" + "album2" #Getting the album folder

        createFolderAndNavigate(browser, "album2", albumFolder)      

        filePaths = []

        #Creating a list of file paths
        for i in range(1, imageNum + 1):
            filePaths.append(imgFile + '\\' + str(i).rjust(3, '0') + ".jpg")

        pages = math.ceil(imageNum / 20) #Getting the number of pages

        for i in range(pages):
            splitedFilePaths = []
            for j in range (i * 20, (i+1) * 20):
                splitedFilePaths.append(filePaths[j]) #Splitting the list of file paths into smaller lists of 20 elements
                if j == imageNum - 1 and i == pages - 1:
                    break

            for i in range(10):
                try: 

                    browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button
                    break
                except ElementNotInteractableException or NoSuchElementException:
                    sleep(0.5);
        
            browser.find_element(By.ID, "upload-file").send_keys('\n'.join(splitedFilePaths)) ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        #clicking start upload button
        for i in range(100):
            try: 
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']") 
                element.click() #Clicking the start upload button
                break;
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)

        albumExists = True

    #Uploading the image 1.jpg
    elif (exists(downloads + '\\' + "1.jpg")) and (len(removeFiles(os.listdir(downloads), downloads)) == 1 or len(removeFiles(os.listdir(downloads), downloads)) == 2): #Check if the 1.jpg file exists in the downloads folder
        albumFolder = folder + "-" + "album" # Getting the album folder

        createFolderAndNavigate(browser, "album", albumFolder)      

        for i in range(10):
            try: 
                browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button and clicking it
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);
        
        browser.find_element(By.ID, "upload-file").send_keys(downloads + '\\' + "1.jpg") ##Getting the input button and uploading the images

        logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

        for i in range(10):
            try:    
                element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']") 
                element.click() #Clicking the start upload button
                break
            except ElementNotInteractableException or NoSuchElementException:
                sleep(0.5);

        albumExists = True

    #Uploading the images from "Album"
    elif (exists(imgFile) and imageNum > 1):

        albumFolder = folder + "-" + "album" #Getting the album folder

        createFolderAndNavigate(browser, "album", albumFolder)            

        filePaths = []

        #Creating a list of file paths
        for i in range(1, imageNum + 1):
            filePaths.append(imgFile + '\\' + str(i).rjust(3, '0') + ".jpg")


        pages = math.ceil(imageNum / 20) #Getting the number of pages

        for i in range(pages):
            splitedFilePaths = []
            for j in range (i * 20, (i+1) * 20):
                splitedFilePaths.append(filePaths[j]) #Splitting the list of file paths into smaller lists of 20 elements
                if j == imageNum - 1 and i == pages - 1:
                    break

            for i in range(10):
                try: 

                    browser.find_element(By.XPATH, "//button[text()=' Upload']").click() #Getting the upload button
                    break
                except ElementNotInteractableException or NoSuchElementException:
                    sleep(0.5);
        
            browser.find_element(By.ID, "upload-file").send_keys('\n'.join(splitedFilePaths)) ##Getting the input button and uploading the images

            logo = browser.find_element(By.CLASS_NAME, "logo") #Getting the logo for scrolling purposes

            browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

            for i in range(10):
                try:    
                    element = browser.find_element(By.XPATH, "//button[text()=' Start Upload']") 
                    element.click() #Clicking the start upload button
                    break
                except ElementNotInteractableException or NoSuchElementException:
                    sleep(0.5);

        albumExists = True

    return naslovnaExists, albumExists