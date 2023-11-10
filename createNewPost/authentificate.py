
from selenium.webdriver.common.by import By
import json
from time import sleep
from selenium.webdriver.common.keys import Keys

adimnPath = "/administrator"

def authentificate(selectedWebsite, browser, websiteGen):
  file = open(r"C:\Users\jurer\OneDrive\scripts\websitesData\passwords.json", "r")
  passwords = json.load(file)

  password = ""
  username = ""

  #Getting the username and password for the selected website
  for i in passwords:
    if (i["url"] == selectedWebsite):
      username = i["username"]
      password = i["password"]
      break;
  
  browser.get("https://" + selectedWebsite + adimnPath) #Opening the website

  #Getting the username and password fields
  usernameField = browser.find_element(By.ID, "mod-login-username")
  passwordField = browser.find_element(By.ID, "mod-login-password")

  loginBtn = ""
  if websiteGen == 2 or websiteGen == 3 or websiteGen == 4:
    loginBtn = browser.find_element(By.CLASS_NAME, "login-button")
  elif websiteGen == 1:
    loginBtn = browser.find_element(By.CLASS_NAME, "button1")

  #Filling the fields with the username and password
  usernameField.send_keys(username)
  passwordField.send_keys(password)

  loginBtn.click() #Clicking the login button
  sleep(1) #Waiting for the page to load

