from selenium.webdriver.common.by import By
from time import sleep
import datetime
from selenium.common.exceptions import NoSuchElementException

from clickAndNavigate import waitToClick
from clickAndNavigate import scrollAndClick
from clickAndNavigate import click

def createPost(browser, category, folder, postTitle, widgetID, imagesExist, websiteGen, tempFile, tableExist, imageFloat, imageFloatDefault, date):
    #Navigate to the new post page
    navigationElement = browser.find_element(By.LINK_TEXT, 'Content')
    navigationElement.click()

    navigationElement = browser.find_element(By.LINK_TEXT, 'Articles')
    navigationElement.click()

    newPostBtn = browser.find_element(By.CLASS_NAME, 'btn-success') #Clicking on the "New" button
    click(newPostBtn)

    #Finding the naslovna image if it exists for this post
    if (imagesExist[0]):
        imagesAndLinks = browser.find_element(By.LINK_TEXT, "Images and Links") #Clicking on the "Images and Links" tab
        click(imagesAndLinks)

        #articleImageSelect
        selectImg(browser, category, folder, 0, imageFloat, imageFloatDefault, date["year"])

        #fullArticleImgSelect
        selectImg(browser, category, folder, 1, imageFloat, imageFloatDefault, date["year"])

        navigationTabs = browser.find_element(By.CLASS_NAME, "nav-tabs") #Finding the navigation tabs

        contentBtn = navigationTabs.find_element(By.LINK_TEXT, "Content") #Finding the "Content" tab
        click(contentBtn) #Clicking on the "Content" tab

    #Entering the title
    titleInput = browser.find_element(By.ID, "jform_title")
    titleInput.send_keys(postTitle)

    #Entering the widgetID if there is album for this post
    if (imagesExist[1]):
        contentIframe = browser.find_element(By.XPATH, "//iframe[@ID='jform_articletext_ifr']") #Switching to the content iframe
        browser.switch_to.frame(contentIframe)

        contentInput = browser.find_element(By.ID, "tinymce") #Finding the content input
        contentInput.send_keys(widgetID) #Entering the content

        browser.switch_to.default_content() #Switching back to the default content

    #Entering the table if it exists
    if (tableExist):
        toggleBtn = browser.find_element(By.CLASS_NAME, "toggle-editor").find_element(By.XPATH, "*") #Clicking on the "Toggle editor" button
        browser.execute_script("arguments[0].scrollIntoView();", toggleBtn)
        click(toggleBtn)

        contentInput = browser.find_element(By.ID, "jform_articletext") #Finding the content input

        browser.execute_script("arguments[0].scrollIntoView();", contentInput)

        contentInput.send_keys(tempFile.read()) #Entering the content

#Funciton for selecting an image
def selectImg (browser, category, folder, imageOrder, imageFloat, imageFloatDefault, year):
    articleImgSelect = browser.find_elements(By.XPATH, "//button[text()='Select']")

    click(articleImgSelect[imageOrder])
    
    firstIframe = ""
    for i in range(0, 100):
        try:
            firstIframe = browser.find_element(By.XPATH, "//iframe[@name='field-media-modal']") #Switching to the first iframe
            browser.switch_to.frame(firstIframe)
        except NoSuchElementException:
            continue

    secondIframe = browser.find_element(By.XPATH, "//iframe[@name='imageframe']") #Switching to the second iframe
    browser.switch_to.frame(secondIframe)

    #Selecting the category
    categoryLiTags = browser.find_elements(By.CLASS_NAME, "imgOutline")

    for tag in categoryLiTags:
        categoryText = tag.find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[-1].text
        
        categoryNumber = categoryText.split("_")[0]

        if (categoryNumber == category.split("_")[0]):
            tag.click()
            break
        else:
            continue

    #Selecting the year
    yearLiTags = ""
    for i in range(0, 100):
        try:             
            yearLiTags = browser.find_elements(By.CLASS_NAME, "imgOutline")
        except NoSuchElementException:
            sleep(0.1)
            continue

    for tag in yearLiTags:
                elementYear = tag.find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[-1].text

                if (elementYear == str(year)):
                    tag.click()
                    break
                else:
                    continue

    #Selecting the month
    dateLiTags = ""
    for i in range(0, 100):
        try:             
            dateLiTags = browser.find_elements(By.CLASS_NAME, "imgOutline")
        except NoSuchElementException:
            sleep(0.1)
            continue

    for tag in dateLiTags:
                date = tag.find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[-1].text

                if (date == folder):
                    tag.click()
                    break
                else:
                    continue

    #Selecting the image
    waitToClick(browser, "CLASS_NAME", "imgThumbInside")
    
    #Switching to the first iframe for the "Insert" button to be visible
    browser.switch_to.default_content() 
    firstIframe = browser.find_element(By.XPATH, "//iframe[@name='field-media-modal']")
    browser.switch_to.frame(firstIframe)

    browser.find_element(By.CLASS_NAME, "btn-success").click() #Clicking on the "Insert" button

    browser.switch_to.default_content() #Switching to the default content
    
    if ((imageFloatDefault == "Use Global (None)") and (imageFloat == "none")):
        return

    #Clicking on the "Use Global ()" button
    selectFloatXPATH = "//span[text()='" + imageFloatDefault + "']"
    selectFloatSpan = browser.find_elements(By.XPATH, selectFloatXPATH)

    click(selectFloatSpan[0])
    #Clicking the desired float option
    if imageOrder == 1:
        imageFloatSelect = browser.find_element(By.ID, "jform_images_float_fulltext_chzn") #Finding the image float select
        optionsUl = imageFloatSelect.find_elements(By.XPATH, "*")[-1].find_elements(By.XPATH, "*")[-1] #Finding the options ul

        floatOption = ""
        check = "left"
        if (imageFloat == check):
            floatOption = optionsUl.find_elements(By.XPATH, "*")[-2]
        else:
            floatOption = optionsUl.find_elements(By.XPATH, "*")[-1]

        browser.execute_script("window.scrollBy(0, 200)")
        
        click(floatOption)
    else:
        imageFloatSelect = browser.find_element(By.ID, "jform_images_float_intro_chzn") #Finding the image float select
        optionsUl = imageFloatSelect.find_elements(By.XPATH, "*")[-1].find_elements(By.XPATH, "*")[-1] #Finding the options ul

        floatOption = ""
        check = "left"
        if (imageFloat == check):
            floatOption = optionsUl.find_elements(By.XPATH, "*")[-2]
        else:
            floatOption = optionsUl.find_elements(By.XPATH, "*")[-1]

        floatOption.click()

    browser.execute_script("window.scrollBy(0, -200)")
