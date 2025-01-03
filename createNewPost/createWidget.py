from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

from clickAndNavigate import click
from rename import rename
from clickAndNavigate import scrollAndClick
from clickAndNavigate import waitToClick
from rename import rename

def createWidget(browser, imageNum, secondAlbumType, postTitle, folder, category, albumExists, websiteGen, date):
    if (albumExists == False):
        return
    
    newWidgetID = ""
    newWidgetID2 = ""

    #Navigating to the widget creation page
    navigationElement = browser.find_element(By.LINK_TEXT, 'Components')
    navigationElement.click()

    navigationElement = browser.find_element(By.LINK_TEXT, 'Widgetkit')
    navigationElement.click()

    if websiteGen == 3:
        for i in range(0, 100):
            widgetNum = browser.find_elements(By.CLASS_NAME, 'uk-visible-hover-inline')
            if (len(widgetNum) > 0):
                break
            else:
                sleep(0.1)
                continue

    elif websiteGen == 4:
        for i in range(0, 100):
            try: 
                widgetNum = browser.find_elements(By.CLASS_NAME, 'uk-visible-toggle')
                if (len(widgetNum) > 0):
                    break
                else:
                    sleep(0.1)
                    continue
            except NoSuchElementException or ElementNotInteractableException:
                sleep(0.1)

    elif websiteGen == 2:

        galleryBtn = browser.find_element(By.LINK_TEXT, 'Gallery')
        click(galleryBtn)

    #Two albums and two widgets
    if (secondAlbumType == "two_albums"):
        if websiteGen == 3:
            newWidgetID = newWidgetGen3(browser, postTitle, folder, "jedna_slika", category, date["year"])

             #waiting for widgets to load to create second album
            if websiteGen == 3:
                for i in range(0, 100):
                    widgetNum = browser.find_elements(By.CLASS_NAME, 'uk-visible-hover-inline')
                    if (len(widgetNum) > 0):
                        break
                    else:
                        sleep(0.1)
                        continue

            #creating second album
            newWidgetID2 = newWidgetGen3(browser, postTitle + "2", folder, "jedna_slika", category, date["year"], "album2")
        elif websiteGen == 2:
            newWidgetID = newWidgetGen2(browser, postTitle, folder, "jedna_slika", category, date["year"], "album")
            #creating second album
            newWidgetID2 = newWidgetGen2(browser, postTitle + "2", folder, "jedna_slika", category, date["year"], "album2")

    #One image album on top and gallery on the bottom
    elif (secondAlbumType == "main_img_album_and_galery"):
        if websiteGen == 3:
            newWidgetID = newWidgetGen3(browser, postTitle, folder, "jedna_slika", category, date["year"])

             #waiting for widgets to load to create second album
            if websiteGen == 3:
                for i in range(0, 100):
                    widgetNum = browser.find_elements(By.CLASS_NAME, 'uk-visible-hover-inline')
                    if (len(widgetNum) > 0):
                        break
                    else:
                        sleep(0.1)
                        continue

            #creating second album
            newWidgetID2 = newWidgetGen3(browser, postTitle + "2", folder, "album", category, date["year"], "album2")
        elif websiteGen == 2:
            newWidgetID = newWidgetGen2(browser, postTitle, folder, "jedna_slika", category, date["year"], "album")
            #creating second album
            newWidgetID2 = newWidgetGen2(browser, postTitle + "2", folder, "album", category, date["year"], "album2")

    #One image widget
    elif (imageNum == 1):
        if websiteGen == 3:
            newWidgetID = newWidgetGen3(browser, postTitle, folder, "jedna_slika", category, date["year"])
        elif websiteGen == 2:
            newWidgetID = newWidgetGen2(browser, postTitle, folder, "jedna_slika", category, date["year"], "album")
        elif websiteGen == 4:
            newWidgetID = newWidgetGen4(browser, postTitle, folder, "jedna_slika", category, date["year"])

    #Two image widget
    elif (imageNum == 2):
        if websiteGen == 3:
            newWidgetID = newWidgetGen3(browser, postTitle, folder, "dvije_slike", category, date["year"])
        elif websiteGen == 2:
            newWidgetID = newWidgetGen2(browser, postTitle, folder, "dvije_slike", category, date["year"], "album")
        elif websiteGen == 4:
            newWidgetID = newWidgetGen4(browser, postTitle, folder, "dvije_slike", category, date["year"])

    #Album widget
    elif (imageNum > 2):
        if websiteGen == 3:
            newWidgetID = newWidgetGen3(browser, postTitle, folder, "album", category, date["year"])
        elif websiteGen == 2:
            newWidgetID = newWidgetGen2(browser, postTitle, folder, "album", category, date["year"], "album")
        elif websiteGen == 4:
            newWidgetID = newWidgetGen4(browser, postTitle, folder, "album", category, date["year"])
        
    return [newWidgetID, newWidgetID2]


def newWidgetGen2(browser, postTitle, folder, widgetType, category, year, albumName):
    newWidgetID = ""

    allWidgets = browser.find_element(By.ID, "gallery").find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[-1].find_elements(By.XPATH, "*")

    for widget in allWidgets:
        #scrolling to a widget
        browser.execute_script("arguments[0].scrollIntoView();", widget)
        browser.execute_script("window.scrollBy(0, -200)","")

        widgetElement = widget.find_element(By.XPATH, "*").find_element(By.XPATH, "*")

        if (widgetElement.text.endswith(widgetType)):

            copyIcon = widget.find_elements(By.XPATH, "*")[-1].find_elements(By.XPATH, "*")[-2] #Finding the copy icon

            scrollAndClick(browser, copyIcon) #Clicking on the copy icon

            #Getting all the element again after the page reloads
            allWidgets = browser.find_element(By.ID, "gallery").find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[-1].find_elements(By.XPATH, "*")

            newWidget = ""
            for widget in allWidgets:

                widgetElement = widget.find_element(By.XPATH, "*").find_element(By.XPATH, "*")

                if (widgetElement.text.endswith(widgetType)):
                    newWidget = widget.find_element(By.XPATH, "following-sibling::*[1]") #Finding the new widget  
                    break
            
            browser.execute_script("arguments[0].scrollIntoView();", newWidget) #Scrolling to the newWidget
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            newWidgetID = newWidget.find_elements(By.XPATH, "*")[-3].text #Getting the new widget ID

            newWidgetName = newWidget.find_element(By.XPATH, "*").find_element(By.XPATH, "*")

            #Scroling to a new widget
            browser.execute_script("arguments[0].scrollIntoView();", newWidget)
            browser.execute_script("window.scrollBy(0, -200)","")

            click(newWidgetName) #Clicking on the new widget
                       
            newWidgetNameInput = browser.find_element(By.CLASS_NAME, "name") #Finding the widget name input
            newWidgetNameInput.clear() #Clearing the widget name input

            postTitle = rename(postTitle)
       
            splitedPostTitle = postTitle.split("_")[:8]
            splitedPostTitleWithPrefix = ["_" + word for word in splitedPostTitle]

            newWidgetName = str(year) + "_" + folder + "_" + "".join(splitedPostTitleWithPrefix) + "_" + widgetType #Creating the new widget name
   
            newWidgetName = rename(newWidgetName).lower() #Renaming the widget name
            newWidgetNameInput.send_keys(newWidgetName) #Sending the new widget name

            deletePrevImages = browser.find_element(By.CLASS_NAME, "deletable") #Finding the delete previous images checkbox
            deletePrevImages.click() #Clicking on the delete previous images checkbox

            category = browser.find_element(By.LINK_TEXT, category) #Finding the category

            browser.execute_script("arguments[0].scrollIntoView();", category) #Scrolling to the category
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            click(category) #Clicking on the category
            
            element = ""

            #Waiting for the year folder to appear
            for i in range(0, 100):
                try: 
                    element = browser.find_element(By.LINK_TEXT, str(year)) 
                    break
                except NoSuchElementException:
                    sleep(0.1)

            #Finding the year folder and clicking it
            browser.execute_script("arguments[0].scrollIntoView();", element) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            element = waitToClick(browser, "LINK_TEXT", str(year)) #Finding the year folder and clicking it
            
            #Waiting for the folder to appear
            for i in range(0, 100):
                try: 
                    element = browser.find_element(By.LINK_TEXT, str(folder)) 
                    break
                except NoSuchElementException:
                    sleep(0.1)

            #Scroling to the folder and clicking it
            browser.execute_script("arguments[0].scrollIntoView();", element) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            element = waitToClick(browser, "LINK_TEXT", folder) #Finding the date folder and clicking it

            #Waiting for the folder to appear
            for i in range(0, 100):
                try: 
                    element = browser.find_element(By.LINK_TEXT, albumName) 
                    break
                except NoSuchElementException:
                    sleep(0.1)

            #Scroling to the album folder and clicking on it
            browser.execute_script("arguments[0].scrollIntoView();", element) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            element = waitToClick(browser, "LINK_TEXT", albumName) #Finding the album folder and clicking it

            browser.execute_script("arguments[0].scrollIntoView();", element) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            element = browser.find_element(By.XPATH, "//button[text()='Add to Photo Gallery']") #Finding the select button
            browser.execute_script("arguments[0].scrollIntoView();", element) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit
            click(element) #Clicking on the select button

            saveBtn = browser.find_element(By.CLASS_NAME, "btn-success") #Finding the save button
            browser.execute_script("arguments[0].scrollIntoView();", saveBtn) #Scrolling to the element

            #Waiting for album images to load
            for i in range(100):
                try:
                    element = browser.find_element(By.ID, "box") #Finding the album images
                    break
                except NoSuchElementException:
                    sleep(0.1)

            click(saveBtn) #Clicking on the save button

            cancelBtn = browser.find_element(By.CLASS_NAME, "button-cancel") #Finding the cancel button
            click(cancelBtn) #Clicking on the cancel button

            return newWidgetID       

#Creating a new widget for gen3 websites
def newWidgetGen3(browser, postTitle, folder, widgetType, category, year, albumName=None):
    newWidgetID = ""

    allWidgets = browser.find_elements(By.CLASS_NAME, 'uk-visible-hover-inline')

    a = ActionChains(browser)

    for widget in allWidgets:
        widgetElement = widget.find_element(By.XPATH, "*").find_element(By.XPATH, "*")

        #browser.execute_script("arguments[0].scrollIntoView();", widget) #Scrolling to the element
        #browser.execute_script("window.scrollBy(0, 200)") #Scrolling up a bit

        #Finding the first existing widget that ends the same as the widgetType and copying it
        if (widgetElement.text.endswith(widgetType)):
            browser.execute_script("arguments[0].scrollIntoView();", widgetElement) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit
            
            copyIcon = widget.find_elements(By.XPATH, "*")[-1].find_element(By.XPATH, "*") #Finding the copy icon

            a.move_to_element(widgetElement) #Hovering over the copy icon
            a.perform() #Performing the hover action

            copyIcon.click()     #Clicking on the copy icon

            #Waiting for the new widget to appear
            for i in range(0, 100):
                newAllWidgets = browser.find_elements(By.CLASS_NAME, 'uk-visible-hover-inline')   
                if (len(newAllWidgets) > len(allWidgets)):
                    break
                else:
                    sleep(0.1)
                    continue     

            newWidget = widget.find_element(By.XPATH, "following-sibling::*[1]") #Finding the new widget

            newWidgetID = newWidget.find_elements(By.XPATH, "*")[-2].text #Getting the new widget ID
            
            newWidget.find_element(By.XPATH, "*").find_element(By.XPATH, "*").click() #Clicking on the new widget
            #sleep(50)

            newWidgetNameInput = browser.find_element(By.CLASS_NAME, "uk-form-large") #Finding the widget name input

            newWidgetNameInput.clear() #Clearing the widget name input

            postTitle = rename(postTitle)

            splitedPostTitle = postTitle.split("_")[:8]
            splitedPostTitleWithPrefix = ["_" + word for word in splitedPostTitle]

            newWidgetName = str(year) + "_" + folder + "_" + "".join(splitedPostTitleWithPrefix) + "_" + widgetType #Creating the new widget name
 
            newWidgetName = rename(newWidgetName).lower() #Renaming the widget name
            newWidgetNameInput.send_keys(newWidgetName) #Sending the new widget name

            folderPathInput = ""
            for i in range(0, 100):
                try:
                    folderPathInput = browser.find_element(By.ID, "wk-path") #Finding the folder path input
                    break
                except NoSuchElementException:
                    sleep(0.5)
                    continue

            folderPathInput.clear() #Clearing the folder path input

            album = "album"

            if albumName:
                album = albumName

            newFolderPath = "images" + "/" + category + "/" + str(year) + "/" + folder + "/" +  album #Creating the new folder path

            folderPathInput.send_keys(newFolderPath) #Sending the new folder path to the folder path input

            saveButton = browser.find_element(By.XPATH, "//button[text()=' Save & Close']") #Finding the save button
            saveButton.click()  #Clicking on the save button

            return newWidgetID
        else:
            continue

def newWidgetGen4(browser, postTitle, folder, widgetType, category, year):
    newWidgetID = ""

    allWidgets = browser.find_elements(By.CLASS_NAME, 'uk-visible-toggle')

    a = ActionChains(browser)

    for widget in allWidgets:
        #Finding the first existing widget and copying it
    
        widgetElement = widget.find_element(By.XPATH, "*").find_element(By.XPATH, "*")

        if (widgetElement.text.endswith(widgetType)):

            browser.execute_script("arguments[0].scrollIntoView();", widgetElement) #Scrolling to the element
            browser.execute_script("window.scrollBy(0, -200)","") #Scrolling up a bit

            copyIcon = widget.find_elements(By.XPATH, "*")[-1].find_element(By.XPATH, "*").find_element(By.XPATH, "*") #Finding the copy icon

            a.move_to_element(widgetElement) #Hovering over the copy icon
            a.perform() #Performing the hover action
            copyIcon.click()       #Clicking on the copy icon

            #Waiting for the new widget to appear
            for i in range(0, 100):
                newAllWidgets = browser.find_elements(By.CLASS_NAME, 'uk-visible-toggle')   
                if (len(newAllWidgets) > len(allWidgets)):
                    break
                else:
                    sleep(0.1)
                    continue     

            newWidget = widget.find_element(By.XPATH, "following-sibling::*[1]") #Finding the new widget

            newWidgetID = newWidget.find_elements(By.XPATH, "*")[-2].text #Getting the new widget ID
            
            newWidget.find_element(By.XPATH, "*").find_element(By.XPATH, "*").click() #Clicking on the new widget

            newWidgetNameInput = browser.find_elements(By.CLASS_NAME, "uk-input")[0] #Finding the widget name input

            newWidgetNameInput.clear() #Clearing the widget name input

            postTitle = rename(postTitle)

            splitedPostTitle = postTitle.split("_")[:8]
            splitedPostTitleWithPrefix = ["_" + word for word in splitedPostTitle]

            newWidgetName = str(year) + "_" + folder + "_" + "".join(splitedPostTitleWithPrefix) + "_" + widgetType #Creating the new widget name

            newWidgetName = rename(newWidgetName).lower() #Renaming the widget name
            newWidgetNameInput.send_keys(newWidgetName) #Sending the new widget name

            folderPathInput = ""
            for i in range(0, 100):
                try:
                    folderPathInput = browser.find_element(By.ID, "wk-path") #Finding the folder path input
                    break
                except NoSuchElementException:
                    sleep(0.05)
                    continue

            folderPathInput.clear() #Clearing the folder path input

            newFolderPath = "images" + "/" + category + "/" + str(year) + "/" +folder + "/" + "album" #Creating the new folder path

            folderPathInput.send_keys(newFolderPath) #Sending the new folder path to the folder path input

            saveButton = browser.find_element(By.XPATH, "//button[text()=' Save & Close']") #Finding the save button
            saveButton.click()  #Clicking on the save button

            return newWidgetID
        else:
            continue
            