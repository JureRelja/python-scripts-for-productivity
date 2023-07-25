from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
import os

from navToFolder import navigateToNewFolder
from authentificate import authentificate #Importing the function from authentificate.py
from selectWebsite import selectWebsite #Importing the function from selectWebsite.py
from uploadImages import uploadImages #Importing the function from uploadImages.py
from createFilePost import createPost #Importing the function from createImagePost.py
from selectDateYear import selectDateYear #Importing the function from selectDateYear.py
from createHTMLTable import createHTMLTable #Importing the function from createHTMLTable.py

downloads = str(Path.home() / "Downloads") #Path to the downloads folder

os.chdir(downloads)
files = filter(os.path.isfile, os.listdir(downloads))
files = os.listdir(downloads) 
files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)))

#Setting up the webdriver
service = Service("../cromedriver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#options.add_argument('--headless')

selectedWebsite = selectWebsite() #Selecting the website

date = selectDateYear() #Getting the current month, day and year

browser = webdriver.Chrome(service=service, options=options) #Opening the browser

#authentificate(selectedWebsite="promina.hr", browser=browser, websiteGen=2) #Authentificating the user
authentificate(selectedWebsite=selectedWebsite[0]["url"], browser=browser, websiteGen=selectedWebsite[4]) #Authentificating the user

#folder = navigateToNewFolder(browser=browser, categoryName="02_NOVOSTI", websiteGen=2) #Navigating to the folder where the images will be uploaded
folder = navigateToNewFolder(browser=browser, categoryName=selectedWebsite[1]["category"], websiteGen=selectedWebsite[4], date=date) #Navigating to the folder where the images will be uploaded

table = createHTMLTable(files=files, folder=folder[1], categoryName=selectedWebsite[1]["category"], year=folder[2], selectedWebsite=selectedWebsite[0]["url"]) #Creating the HTML table

#imagesExist = uploadFiles(browser=browser, downloads=downloads, imageNum=imageNum, folder=folder[0], websiteGen=selectedWebsite[4]) #Uploading the images
#imagesExist = uploadImages(browser=browser, imgFile=imgFile, downloads=downloads, imageNum=imageNum, folder=folder[0], websiteGen=2) #Uploading the images

#createPost(browser=browser, category=selectedWebsite[1]["category"], folder=folder[1], postTitle=selectedWebsite[2], widgetID=widgetID, imagesExist=imagesExist, imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post
#createPost(browser=browser, category=selectedWebsite[1]["category"], folder="07_06", postTitle=selectedWebsite[2], widgetID="43", imagesExist=[True, True], imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post

sleep(200)


