from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
from selenium.webdriver.chrome.options import Options
import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome()


#this function check if instagram asks to activate notifications
def check_notification_message():
    try:
        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    except NoSuchElementException:
        try:
            time.sleep(4)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        except NoSuchElementException:
            return False
    return True

def check_cookies_message():
    try:
        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    except NoSuchElementException:
        return False
    return True

#This function logs in to instagram with use's credentials
def login_insta(user, message, index, counter, users_arr, messages_arr, username, password):
        
    if index == 0:
        if(check_cookies_message()):
            cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
            cookies.click()
            time.sleep(10)
        try:
            elem = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        finally:      
            instagram_username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            instagram_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            instagram_login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')


        instagram_username.send_keys(username)
        instagram_password.send_keys(password)
        instagram_login_btn.click()
        time.sleep(12)
        enter_messanger(user, message, counter, index, users_arr, messages_arr, username, password)
    else:
        enter_messanger(user, message, counter, index, users_arr, messages_arr, username, password)

            

        
    
    
#Enters the messenger page
def enter_messanger(user, message, counter, index, users_arr, messages_arr, username, password):
    driver.get("https://www.instagram.com/direct/inbox/")
    create_message(user, message, counter, index, users_arr, messages_arr, username, password)



#Creates a new message
def create_message(user, message, counter, index, users_arr, messages_arr, username, password):
    if (check_notification_message()):
        try:
            not_now = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            not_now.click()
        except NoSuchElementException:
            not_now = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            not_now.click()
        try:
            elem = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role = 'button']")))
        finally:  
            create_new_message_btn = driver.find_elements(By.CSS_SELECTOR, "div[role = 'button']")
            for e in create_new_message_btn:
                if e.text == "Send message":
                    e.click()
                    search_user(user, message, counter, index, users_arr, messages_arr, username=username, password=password)
    else:
        try:
            elem = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role = 'button']")))
        finally:  
            create_new_message_btn = driver.find_elements(By.CSS_SELECTOR, "div[role = 'button']")
            for e in create_new_message_btn:
                if e.text == "Send message":
                    e.click()
                    search_user(user, message, counter, index, users_arr, messages_arr, username=username, password=password)



#Searching a user 
def search_user(user, message, counter,index, users_arr, messages_arr, username, password):
    try:
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))
    finally:
        to_input = driver.find_element(By.NAME, 'queryBox')
        to_input.send_keys(user)
        press_checkbox(message, counter, index, users_arr, messages_arr, username=username, password=password)

        



#chooses the first option
def press_checkbox(message, counter, index, users_arr, messages_arr, username, password):
    try:
        try:
            WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, 'ContactSearchResultCheckbox')))
        finally:
            user_checkboxes = driver.find_elements(By.NAME, 'ContactSearchResultCheckbox')
            for checkbox in user_checkboxes:
                checkbox.click()
                break
            start_chat(message, counter, index, users_arr, messages_arr,username=username, password=password)
    except NoSuchElementException:
        index += 1
        run_program(user= users_arr[index], message= messages_arr[index], index= index, counter= counter, users_arr= users_arr, messages_arr=messages_arr, username=username, password=password)

#Choose the message text    
def start_chat(message, counter, index, users_arr, messages_arr,username, password):
    try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role = 'button']")))
    finally:
        chat_btn = driver.find_elements(By.CSS_SELECTOR, "div[role = 'button']")
        for button in chat_btn:
            if button.text == "Chat":
                button.click()
                write_a_message(message, counter, index, users_arr, messages_arr, username=username, password=password)



def write_a_message(message, counter, index, users_arr, messages_arr,username, password):
    try:
        WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role = 'textbox']")))
    finally:
        message_box = driver.find_element(By.CSS_SELECTOR, "div[role = 'textbox']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(10)
        move_to_another_page(counter, index, users_arr, messages_arr,username, password)
        

def move_to_another_page(counter, index, users_arr, messages_arr, username, password):
    urls_arr = ['https://www.instagram.com/', 'https://www.instagram.com/explore/', 'https://www.instagram.com/reels/']
    driver.get(random.choice(urls_arr))
    time.sleep(5)
    if index < len(users_arr):
        counter += 1
        index += 1
        run_program(user= users_arr[index], message= messages_arr[index], index= index, counter= counter, users_arr= users_arr, messages_arr=messages_arr, username=username, password=password)

    
def run_program(user, message, index, counter, users_arr, messages_arr, username, password):
    driver.get("https://www.instagram.com/")
    login_insta(user, message, index, counter, users_arr, messages_arr, username, password)


def create_list_and_run(sheet, first_run, username, password):
    cols = ["Users", "Messages"]
    data = pd.read_csv(sheet, usecols=cols)
    users_arr = data.Users.values.tolist()
    messages_arr = data.Messages.values.tolist()
    if(first_run):
        index = 0
        message_counter = 0
        first_run = False
    run_program(user= users_arr[index], message= messages_arr[index], index= index, counter = message_counter, users_arr= users_arr, messages_arr=messages_arr, username=username, password=password)


# create_list_and_run("Untitled spreadsheet - Sheet1.csv", first_run)

