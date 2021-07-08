import random
from selenium.webdriver.chrome.options import Options
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
import datetime
import time
import os.path
from os import path
from selenium.webdriver.common.keys import Keys
import pickle
from random import randrange

# TODO: Follow from earliest followed, use code from sublmine unfollow fuction while loop
# TODO: don't follow people previously followed
# TODO: Find a way to determine how many people were followed over the 3 day period and unfollow that exact amount
# TODO: Determine which followers are actively viewing stories and unfollow those who are not
# TODO: Don't unfollow/follow certain accounts
email = 'someEmail@gmail.com'
pass1 = "SomePassword"
followingPage = "https://www.instagram.com/ACCOUNTNAME"
username = ""
password = ""
loginButton = ""


def getFollowingCount():
    if not driver.current_url == followingPage:
        driver.get(followingPage)
    count = driver.find_element_by_css_selector(
        "#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span")
    return int(count.text)


def unFollow(amount):
    if not driver.current_url == followingPage:
        driver.get(followingPage)
    following = ""
    try:
        following = driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(3) > a")
        following.click()
    except TimeoutException:
        print("Unfollow 1 Problem")

    for i in range(amount):
        firstFollowing = ''
        flag = False
        while not flag:
            try:
                firstFollowing = driver.find_element_by_css_selector(
                    'body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(' + str(
                        i + 1) + ') > div > '
                                 'div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl')
                firstFollowing.click()
                flag = True
            except:
                print("Unfollow 2 Problem")

        unfollowConfirm = ''
        try:
            unfollowConfirm = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
            unfollowConfirm.click()
        except:
            print("Unfollow 3 Problem")
        time.sleep(randrange(25))


def getLoginSession(email, pass1):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.instagram.com/')
    try:
        username = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
        password = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')))
        loginButton = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')))
    except TimeoutException:
        print("Login Session 1 Problem")

    username.send_keys(email)
    password.send_keys(pass1)
    loginButton.click()
    flag = False
    while not flag:
        try:
            username = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > '
                                      'div.pbgfb.Di7vw > div')))
            flag = True
        except:
            print("Login Session 2 Problem")

    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))


def getPost():
    list1 = [1, 2, 3]
    i = random.choice(list1)
    driver.get("https://www.instagram.com/explore/")
    p = ''
    flag = False
    while not flag:
        try:
            p = driver.find_element_by_css_selector(
                "#react-root > section > main > div > div.K6yM_ > div > div:nth-child(1) > div:nth-child(2) > div > a "
                "> "
                "div > div._9AhH0")
            p.click()
            flag = True
        except:
            print("Get Post 1 Problem")
    return driver.current_url


def follow(amount):
    following = ""
    counter = 0
    for i in range(amount):
        flag = False
        while not flag:
            try:
                if counter > 50:
                    break
                following = driver.find_element_by_css_selector(
                    "body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div > div > div:nth-child(" + str(
                        i + 1) + ") > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl")
                following.click()
                flag = True
            except:
                print("Follow 1 Problem")
                counter += 1
        time.sleep(randrange(25))


def finalFollow(amnt):
    post = getPost()

    print(post)

    liked = ''
    flag = False
    while not flag:
        try:
            liked = driver.find_element_by_css_selector(
                'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > a')
            liked.click()
            flag = True
        except:
            print("Final Follow 1 Problem")

    follow(amnt)


try:
    outerFlag = False
    file = open("dayCounter.txt", "r")
    dayCount = int(file.read())
    file.close()
    file = open("hourCounter.txt", "r")
    counter = int(file.read())
    file.close()

    while True:
        changeAmount = 12
        if not path.exists("cookies.pkl"):
            getLoginSession(email, pass1)
        else:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(options=options)
            driver.get('https://www.instagram.com/')
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get('https://www.instagram.com/')
        print("Hour Counter: " + str(counter))
        print("Day Counter: " + str(dayCount + 1))
        # Find way to restart program if chrome crashes

        if dayCount < 3:
            unFollow(changeAmount)
        elif dayCount >= 3:
            finalFollow(changeAmount * 3)
        counter += 1

        if counter >= 24:
            counter = 0
            dayCount += 1

        if dayCount == 8:
            dayCount = 0
        print("Hour Counter: " + str(counter))
        print("Day Counter: " + str(dayCount + 1))
        time.sleep(2)
        driver.close()

        open("hourCounter.txt", "w").close()
        open("dayCounter.txt", "w").close()

        file = open("hourCounter.txt", "r+")
        file.write(str(counter))
        file.close()

        file = open("dayCounter.txt", "r+")
        file.write(str(dayCount))
        file.close()
        time.sleep(3600)
except Exception as e:
    webhook = DiscordWebhook(url="DiscordWebhook",
                             content='Something went wrong \n Error: ' + str(e))
    response = webhook.execute()
