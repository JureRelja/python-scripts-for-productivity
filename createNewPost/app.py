from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
import os
import tempfile

from navToFolder import navigateToNewFolder
from resize import resize #Importing the function from resize.py
from authentificate import authentificate #Importing the function from authentificate.py
from selectWebsite import selectWebsite #Importing the function from selectWebsite.py
from uploadImages import uploadImages #Importing the function from uploadImages.py
from createWidget import createWidget #Importing the function from createWidget.py
from createPost import createPost #Importing the function from createImagePost.py
from selectDateYear import selectDateYear #Importing the function from selectDateYear.py
from createHTMLTable import createHTMLTable #Importing the function from createHTMLTable.py
from deleteFiles import deleteFiles #Importing the function from deleteFiles.py
from uploadFiles import uploadFiles #Importing the function from uploadImages.py
from manipulateFiles import manipulateFiles #Importing the function from manipulateFiles.py

downloads = str(Path.home() / "Downloads") #Path to the downloads folder
imgFile = str(Path.home() / "Downloads/Album") #Path to the folder where the images will be stored

#Adding all the files from the downloads folder to the files list
os.chdir(downloads)
files = filter(os.path.isfile, os.listdir(downloads))
files = os.listdir(downloads) 
files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)))

for file in files:
    if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")) or file == "Album" or file == "desktop.ini": 
        files.remove(file)

tempFile = tempfile.TemporaryFile(mode='w+t', encoding="utf-8")

print(files)

#Setting up the webdriver
service = Service("../cromedriver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#options.add_argument('--headless')

selectedWebsite = selectWebsite() #Selecting the website

date = selectDateYear() #Getting the current month, day and year

imageNum = resize(downloads, imgFile); #Resizing the images

filesExist = manipulateFiles(files=files, downloads=downloads, selectedWebsite=selectedWebsite[0]["url"]) #Manipulating the files

browser = webdriver.Chrome(service=service, options=options) #Opening the browser

authentificate(selectedWebsite=selectedWebsite[0]["url"], browser=browser, websiteGen=selectedWebsite[4]) #Authentificating the user

folder = navigateToNewFolder(browser=browser, categoryName=selectedWebsite[1]["category"], websiteGen=selectedWebsite[4], date=date) #Navigating to the folder where the images will be uploaded

filesExist = uploadFiles(browser=browser, files=files, websiteGen=selectedWebsite[4], downloads=downloads) #Uploading the files

imagesExist = uploadImages(browser=browser, imgFile=imgFile, downloads=downloads, imageNum=imageNum, folder=folder[0], websiteGen=selectedWebsite[4]) #Uploading the images

widgetID = createWidget(browser=browser, imageNum=imageNum, postTitle=selectedWebsite[2], folder=folder[1], category=selectedWebsite[1]["category"], albumExists=imagesExist[1], websiteGen=selectedWebsite[4], date=date) #Creating the widget

tableExist = createHTMLTable(files=files, categoryName=selectedWebsite[1]["category"], year=date["year"], folder=folder[1], tempFile=tempFile, selectedWebsite=selectedWebsite[0]["url"]) #Creating the HTML table
tempFile.seek(0)

createPost(browser=browser, category=selectedWebsite[1]["category"], folder=folder[1], postTitle=selectedWebsite[2], widgetID=widgetID, tempFile=tempFile, imagesExist=imagesExist, tableExist=tableExist, imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post

deleteFiles(downloads=downloads)

tempFile.close()

sleep(2000)


