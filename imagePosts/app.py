from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

from navToFolder import navigateToNewFolder
from resize import resize #Importing the function from resize.py
from authentificate import authentificate #Importing the function from authentificate.py
from selectWebsite import selectWebsite #Importing the function from selectWebsite.py
from uploadImages import uploadImages #Importing the function from uploadImages.py
from createWidget import createWidget #Importing the function from createWidget.py
from createImagePost import createPost #Importing the function from createImagePost.py
from selectDateYear import selectDateYear #Importing the function from selectDateYear.py

downloads = str(Path.home() / "Downloads") #Path to the downloads folder
imgFile = str(Path.home() / "Downloads/Album") #Path to the folder where the images will be stored

#Setting up the webdriver
service = Service("../cromedriver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#options.add_argument('--headless')

selectedWebsite = selectWebsite() #Selecting the website

date = selectDateYear() #Getting the current month, day and year

imageNum = resize(downloads, imgFile); #Resizing the images

browser = webdriver.Chrome(service=service, options=options) #Opening the browser

#authentificate(selectedWebsite="promina.hr", browser=browser, websiteGen=2) #Authentificating the user
authentificate(selectedWebsite=selectedWebsite[0]["url"], browser=browser, websiteGen=selectedWebsite[4]) #Authentificating the user

#folder = navigateToNewFolder(browser=browser, categoryName="02_NOVOSTI", websiteGen=2) #Navigating to the folder where the images will be uploaded
folder = navigateToNewFolder(browser=browser, categoryName=selectedWebsite[1]["category"], websiteGen=selectedWebsite[4], date=date) #Navigating to the folder where the images will be uploaded

imagesExist = uploadImages(browser=browser, imgFile=imgFile, downloads=downloads, imageNum=imageNum, folder=folder[0], websiteGen=selectedWebsite[4]) #Uploading the images
#imagesExist = uploadImages(browser=browser, imgFile=imgFile, downloads=downloads, imageNum=imageNum, folder=folder[0], websiteGen=2) #Uploading the images

widgetID = createWidget(browser=browser, imageNum=imageNum, postTitle=selectedWebsite[2], folder=folder[1], category=selectedWebsite[1]["category"], albumExists=imagesExist[1], websiteGen=selectedWebsite[4], date=date) #Creating the widget
#widgetID = createWidget(browser=browser, imageNum=imageNum, postTitle="Nova objava", folder=folder[1], category="02_NOVOSTI", albumExists=imagesExist[1], websiteGen=2, year="2023") #Creating the widget

createPost(browser=browser, category=selectedWebsite[1]["category"], folder=folder[1], postTitle=selectedWebsite[2], widgetID=widgetID, imagesExist=imagesExist, imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post
#createPost(browser=browser, category=selectedWebsite[1]["category"], folder="07_06", postTitle=selectedWebsite[2], widgetID="43", imagesExist=[True, True], imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post

sleep(200)


