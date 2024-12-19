from pathlib import Path
from time import sleep
from selenium.webdriver.common.by import By
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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

filesForDeleting = files.copy()
filesForDeleting.remove("desktop.ini")
filesForDeleting.append("Album")

filesLenght = len(files) #Getting the number of files in the downloads folder
i = 0
while i < filesLenght:
    if filesForDeleting[i].endswith(".xlsx") or filesForDeleting[i].endswith(".zip") or filesForDeleting[i].endswith(".rar") or filesForDeleting[i].endswith(".xls") or filesForDeleting[i].endswith(".csv") or filesForDeleting[i].endswith(".docx") or filesForDeleting[i].endswith(".pdf") or filesForDeleting[i].endswith(".doc") or filesForDeleting[i].endswith(".ods") or filesForDeleting[i].endswith(".odt") or filesForDeleting[i].endswith(".rtf"): 
        filesForDeleting.pop(i)
        i -= 1
        filesLenght -= 1
    i += 1

tempFile = tempfile.TemporaryFile(mode='w+t', encoding="utf-8")

selectedWebsite = selectWebsite() #Selecting the website

date = selectDateYear() #Getting the current month, day and year

imageNum = resize(downloads, imgFile, websiteGen=selectedWebsite[4]); #Resizing the images

filesLenght = len(files) #Getting the number of files in the downloads folder
i = 0
while i < filesLenght:
    if files[i].endswith(".jpg") or files[i].endswith(".JPG") or files[i].endswith(".png") or files[i].endswith(".PNG") or files[i].endswith(".jpeg") or files[i].endswith(".JPEG") or files[i] == "Album" or files[i] == "desktop.ini" or files[i] == "Thumbs.db": 
        files.pop(i)
        i -= 1
        filesLenght -= 1
    i += 1

filesExist = manipulateFiles(files=files, downloads=downloads, selectedWebsite=selectedWebsite[0]["url"], categoryName=selectedWebsite[1]["category"], postTitle=selectedWebsite[2]) #Manipulating the files

tempFile.read()
for file in files:
    filesForDeleting.append(file["fileName"])

#Setting up the webdriver
chrome_install = ChromeDriverManager().install()

folder = os.path.dirname(chrome_install)
folder = os.path.dirname(folder)
chromedriver_path = os.path.join(folder, "chromedriver.exe")

service = ChromeService(chromedriver_path)

#Setting up the webdriver
browser = webdriver.Chrome(service=service)
browser.maximize_window()

authentificate(selectedWebsite=selectedWebsite[0]["url"], browser=browser, websiteGen=selectedWebsite[4]) #Authentificating the user

folder = navigateToNewFolder(browser=browser, categoryName=selectedWebsite[1]["category"], subCategory=selectedWebsite[6], websiteGen=selectedWebsite[4], date=date) #Navigating to the folder where the images will be uploaded

uploadFiles(browser=browser, files=files, filesExist=filesExist, websiteGen=selectedWebsite[4], downloads=downloads) #Uploading the files

imagesExist = uploadImages(browser=browser, imgFile=imgFile, downloads=downloads, imageNum=imageNum[0], secondAlbumType=imageNum[1], folder=folder[0], websiteGen=selectedWebsite[4]) #Uploading the images

widgetID = createWidget(browser=browser, imageNum=imageNum[0], secondAlbumType=imageNum[1], postTitle=selectedWebsite[2], folder=folder[1], category=selectedWebsite[1]["category"], albumExists=imagesExist[1], websiteGen=selectedWebsite[4], date=date) #Creating the widget

tableExist = createHTMLTable(files=files, categoryName=selectedWebsite[1]["category"], subCategory=selectedWebsite[6], filesExist=filesExist, year=date["year"], folder=folder[1], tempFile=tempFile, selectedWebsite=selectedWebsite[0]["url"]) #Creating the HTML table
tempFile.seek(0)

createPost(browser=browser, category=selectedWebsite[1]["category"], folder=folder[1], postTitle=selectedWebsite[2], widgetID=widgetID, tempFile=tempFile, imagesExist=imagesExist, tableExist=tableExist, imageFloat=selectedWebsite[3], imageFloatDefault=selectedWebsite[5], websiteGen=selectedWebsite[4], date=date) #Creating the post

deleteFiles(downloads=downloads, files=filesForDeleting) #Deleting all the files in the downloads folder

tempFile.close()

sleep(2000)


