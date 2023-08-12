
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import datetime
from time import sleep
import string

from clickAndNavigate import scrollAndClick
from clickAndNavigate import click

adimnPath = "/administrator"

def navigateToNewFolder(browser, categoryName, subCategory, websiteGen, date):

    currentDateFolder = str(date["month"]).rjust(2, '0') + "_" + str(date["day"]).rjust(2, '0') #Adding leading zeros to the day and month

    navigationElement = browser.find_element(By.LINK_TEXT, 'Content')
    navigationElement.click()

    if websiteGen == 2 or websiteGen == 3 or websiteGen == 4:
        navigationElement = browser.find_element(By.LINK_TEXT, 'Media')
    elif websiteGen == 1:
        navigationElement = browser.find_element(By.LINK_TEXT, 'Media Manager')

    click(navigationElement)
    
    #Navigating to the folder for gen 2 and 3 websites
    if websiteGen == 2 or websiteGen == 3 or websiteGen == 4:

        yearFolder = "" #ID of the <li> tag that contains the folder for the current year

        if subCategory != "":
            yearFolder = categoryName + "-" + subCategory + "-" + str(date["year"]) #ID of the <li> tag that contains the folder for the current year
        else:
            yearFolder = categoryName + "-" + str(date["year"]) #ID of the <li> tag that contains the folder for the current year

        for i in range(0, 10):
            try: 
                categoryFolder = browser.find_element(By.LINK_TEXT, categoryName) #Getting the cattegory folder
                scrollAndClick(browser, categoryFolder)
                break;
            except NoSuchElementException:
                sleep(0.1)

        if (subCategory != ""):
            for i in range(0, 10):
                try: 
                    categoryFolder = browser.find_element(By.LINK_TEXT, subCategory) #Getting the cattegory folder
                    scrollAndClick(browser, categoryFolder)
                    break;
                except NoSuchElementException:
                    sleep(0.1)

        try:
            liTag = browser.find_element(By.ID, yearFolder) #Checking if the current year folder exists in the category folder
            scrollAndClick(browser, liTag.find_element(By.XPATH, "*")) #If it does, click on it
            sleep(1)
        except NoSuchElementException: 
            createFolderAndNavigate(browser, str(date["year"]), yearFolder) #If it doesn't, create it and click on it

        navigationFolder = yearFolder + "-" + currentDateFolder 
        
        for letter in string.ascii_lowercase:
            if (letter == "a"):
                continue
            try:
                folder = browser.find_element(By.ID, navigationFolder)
                
                if (letter > "b"): 
                    currentDateFolder = currentDateFolder[:- 2] + "_" + letter 
                else:
                    currentDateFolder = currentDateFolder + "_" + letter

                navigationFolder = yearFolder + "-" + currentDateFolder
            except NoSuchElementException:
                break
                
        createFolderAndNavigate(browser, currentDateFolder, navigationFolder)

        return navigationFolder, currentDateFolder, date["year"]

    #Navigating to the folder for gen 1 websites
    elif websiteGen == 1:
        categoryParent = browser.find_element(By.ID, "media-tree_tree").find_elements(By.XPATH, "*")[-1] #Getting the parent of the category folder

        categoryElements = categoryParent.find_elements(By.XPATH, "*") #Getting the category folders

        categoryElement = ""

        for element in categoryElements: #Finding the category folder
            if element.find_elements(By.XPATH, "*")[-1].text == categoryName:
                categoryElement = element
                scrollAndClick(browser, element.find_elements(By.XPATH, "*")[-3].find_element(By.CLASS_NAME, "mooTree_img")) #Expanding the category folder
                break   

        logo = browser.find_element(By.CLASS_NAME, "logo")
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo
        
        yearFolder = categoryElement.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")[-2] #Getting the folder for the current year

        if yearFolder.find_elements(By.XPATH, "*")[-1].text == str(2024): #Checking if the current year folder exists in the category folder
           scrollAndClick(browser, yearFolder.find_elements(By.XPATH, "*")[-1])  #If it does, click on it

        else: 
            click(categoryElement)

            folderInputField = browser.find_element(By.ID, "foldername") #Getting the input field for the folder name
            folderInputField.send_keys(str(2024)) #Filling the input field with the current year

            createFolderButton = browser.find_element(By.XPATH, "//button[text()='Create Folder']") #Getting the create folder button
            createFolderButton.click() #Clicking the create folder button
        
            #Going back the the just created folder
            categoryParent = browser.find_element(By.ID, "media-tree_tree").find_elements(By.XPATH, "*")[-1] #Getting the parent of the category folder
            categoryElements = categoryParent.find_elements(By.XPATH, "*") #Getting the category folders
            categoryElement = ""

            for element in categoryElements: #Finding the category folder
                if element.find_elements(By.XPATH, "*")[-1].text == categoryName:
                    categoryElement = element
                    scrollAndClick(browser, element.find_elements(By.XPATH, "*")[-3]) #Expanding the category folder
                    break   

            logo = browser.find_element(By.CLASS_NAME, "logo")
            browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo
            print("Year folder created")
            yearFolder = categoryElement.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")[-2]
            print(yearFolder.text)
            scrollAndClick(browser, yearFolder) #Expanding the year folder

            browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo

        #Checking if the current date folder exists in the current year folder
        if len(yearFolder.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")) != 0:
            folderDate = yearFolder.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")[-2].find_elements(By.XPATH, "*")[-1].text
            
            existingFolderDate = folderDate.split("_")[0] + "_" + folderDate.split("_")[1]
            existingLetter = folderDate.split("_")[-1]

            if currentDateFolder == existingFolderDate: #If the last folder created was created today, add a corresponding letter to the folder name
                for letter in string.ascii_lowercase:
                    if (letter == "a"):
                        continue

                    if (letter < existingLetter):
                        continue
                    
                    if (letter == existingLetter):
                        continue
                    currentDateFolder = currentDateFolder + "_" + letter
                    break
        
        folderInputField = browser.find_element(By.ID, "foldername") #Getting the input field for the folder name
        folderInputField.send_keys(currentDateFolder) #Filling the input field with the current year

        createFolderButton = browser.find_element(By.XPATH, "//button[text()='Create Folder']") #Getting the create folder button
        createFolderButton.click() #Clicking the create folder button
        
        #Going back the the just created folder
        categoryParent = browser.find_element(By.ID, "media-tree_tree").find_elements(By.XPATH, "*")[-1] #Getting the parent of the category folder
        categoryElements = categoryParent.find_elements(By.XPATH, "*") #Getting the category folders
        categoryElement = ""
        
        for element in categoryElements: #Finding the category folder
            if element.find_elements(By.XPATH, "*")[-1].text == categoryName:
                categoryElement = element
                scrollAndClick(browser, element.find_elements(By.XPATH, "*")[-3].find_element(By.CLASS_NAME, "mooTree_img")) #Expanding the category folder
                break   

        logo = browser.find_element(By.CLASS_NAME, "logo")
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo

        yearFolder = categoryElement.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")[-2]

        scrollAndClick(browser, yearFolder) #Expanding the year folder

        dateFolder = yearFolder.find_element(By.XPATH, "following-sibling::*[1]").find_elements(By.XPATH, "*")[-2] #Getting the date folder
        
        scrollAndClick(browser, dateFolder) #Clicking the date folder
        browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo

    return currentDateFolder


def createFolderAndNavigate(browser, createFolderName, nagivateFolderName):
    #Getting the logo for scrolling purposes
    logo = browser.find_element(By.CLASS_NAME, "logo")

    browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the logo so that the create folder button is visible

    browser.find_element(By.XPATH, "//button[text()=' Create New Folder']").click() #Clicking the create folder button

    folderNameInput = browser.find_element(By.ID, "foldername") #Getting the input field for the folder name
    folderNameInput.send_keys(createFolderName) #Filling the input field with the current year
    
    browser.execute_script("arguments[0].scrollIntoView();", logo) #Scrolling to the details tag so that the create folder button is visible

    browser.find_element(By.XPATH, "//button[text()=' Create Folder']").click() #Clicking the create folder button

    for i in range(100):
        try: 
            folder = browser.find_element(By.ID, nagivateFolderName).find_element(By.XPATH, "*") #Getting the newly created folder for the current year
            scrollAndClick(browser, folder)
            break;
        except NoSuchElementException or ElementNotInteractableException:
            sleep(0.5)

    sleep(2)



