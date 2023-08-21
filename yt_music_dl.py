from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import bs4 as bs
import requests
import sys
import os
import functools
from string import punctuation


def check_url(url):
    r = requests.get(url)

    def check_connection(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if r.status_code == 200:
                print("status > OK")
                func()
            else:
                print("check your connection")
        return wrapper


# selenium way
tag = "h1"
delay = 3
save_path = "/home/flu/Project/module/test"


op = webdriver.ChromeOptions()
op.add_experimental_option("prefs", {"download.default_directory": save_path})
# op.add_argument("headless")
driver = webdriver.Chrome(
    "/home/flu/.web_driver/chromedriver-linux64/chromedriver")
driver.get(
    "https://api.y2convert.net/api/single/mp3?url=https://youtu.be/n0ciQf4HDxg")


try:
    e = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.TAG_NAME, tag)))
    if "convert" in e.text.lower().split():
        download_page = driver.window_handles[0]
        e.click()
        # sleep(30)
        driver.switch_to.window(window_name=download_page)
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.TAG_NAME, tag)))
            sleep(10)
            e2 = driver.find_element(by=By.TAG_NAME, value=tag)
            if "download" in e2.text.lower().split():
                e2.click()
                download_name = driver.find_element(
                    by=By.TAG_NAME, value="h2").text
                print(download_name)
                while True:
                    sep = download_name.rfind("-")
                    size = download_name[sep:]
                    download_name = download_name[:sep].strip()
                    download_name = download_name.translate(
                        str.maketrans(" ", " ", punctuation))
                    for item in os.listdir(save_path):
                        if all([i.strip() for i in download_name.split()]) in [i.strip() for i in item.split()]:
                            print(f"Downloaded > {save_path}")
                            driver.quit()
                            break
                    sleep(3)
            else:
                print("Download> PageError")
        except TimeoutException:
            print("Download> TimedOut")
    else:
        print("Convert> PageError")
except TimeoutException:
    print("Convert> TimedOut")


# requests
# value = "n0ciQf4HDxg"
# req = f"/convert?url=https%3A%2F%2Fyoutu.be%2F{value}"
# # r = requests.get(f"https://y2convert.net{req}")
# # print(r.content)
# # r2 = requests.get(
# #     "https://api.y2convert.net/api/single/mp3?url=https://youtu.be/n0ciQf4HDxg")
# # print(r2.status_code)
# # print(r2.content)
# ro = requests.options(url="https://dl--master--cdn.ytapis.com/api/json", params={"Accept": "*/*",
#                                                                                  "Access-Control-Request-Method": "POST",
#                                                                                  "Access-Control-Request-Headers": "content-type",
#                                                                                  "Origin": "https://api.y2convert.net",
#                                                                                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
#                                                                                  "Sec-Fetch-Mode": "cors",
#                                                                                  "Sec-Fetch-Site": "cross-site",
#                                                                                  "Sec-Fetch-Dest": "empty",
#                                                                                  "Referer": "https://api.y2convert.net/",
#                                                                                  "Accept-Encoding": "gzip, deflate",
#                                                                                  "Accept-Language": "en-US,en;q=0.9"})
# print(ro.status_code)
# print(ro.content)


# cli interface
# to mp4
# to mp3
# search and then mp3 or mp4

# path to save
