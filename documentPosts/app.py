from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
import os
import tempfile

from navToFolder import navigateToNewFolder
from authentificate import authentificate #Importing the function from authentificate.py
from selectWebsite import selectWebsite #Importing the function from selectWebsite.py
from uploadFiles import uploadFiles #Importing the function from uploadImages.py
from createFilePost import createPost #Importing the function from createImagePost.py
from selectDateYear import selectDateYear #Importing the function from selectDateYear.py
from createHTMLTable import createHTMLTable #Importing the function from createHTMLTable.py
from deleteFiles import deleteFiles #Importing the function from deleteFiles.py

downloads = str(Path.home() / "Downloads") #Path to the downloads folder

os.chdir(downloads)
files = filter(os.path.isfile, os.listdir(downloads))
files = os.listdir(downloads) 
files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)))

for file in files:
    if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
        files.remove(file)

tempFile = tempfile.NamedTemporaryFile()

#Setting up the webdriver
service = Service("../cromedriver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#options.add_argument('--headless')

selectedWebsite = selectWebsite() #Selecting the website

date = selectDateYear() #Getting the current month, day and year

browser = webdriver.Chrome(service=service, options=options) #Opening the browser

authentificate(selectedWebsite=selectedWebsite[0]["url"], browser=browser, websiteGen=selectedWebsite[4]) #Authentificating the user

folder = navigateToNewFolder(browser=browser, categoryName=selectedWebsite[1]["category"], websiteGen=selectedWebsite[4], date=date) #Navigating to the folder where the images will be uploaded

tableExist = createHTMLTable(files=files, folder=folder[1], categoryName=selectedWebsite[1]["category"], year=folder[2], downloads=downloads, tempFile=tempFile, selectedWebsite=selectedWebsite[0]["url"]) #Creating the HTML table

filesExist = uploadFiles(browser=browser, files=files, websiteGen=selectedWebsite[4]) #Uploading the files

createPost(browser=browser, category=selectedWebsite[1]["category"], folder="07_06", postTitle=selectedWebsite[2], tempFile=tempFile, widgetID="43", imagesExist=[True, True], imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post

tempFile.close()
deleteFiles(downloads=downloads)

sleep(200)


