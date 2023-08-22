from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as e
from selenium.webdriver.chrome.service import Service
from sys import argv
import os
from functools import wraps
import requests
from slp import Slp


def check_url(url):
    r = requests.get(url)

    def check_connection(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if r.status_code == 200:
                print("status > OK")
                func(*args, **kwargs)
            else:
                print("conectionError> check your connection")
        return wrapper
    return check_connection


@check_url("https://dl--master--cdn.ytapis.com/")
def main(search: str = "", save_path: str = "", u: bool = False):
    if u:
        url = f"https://dl--master--cdn.ytapis.com/api/widget?url={search}"
    else:
        url = "https://dl--master--cdn.ytapis.com/"
    op = webdriver.ChromeOptions()
    if len(save_path) != 0:
        op.add_experimental_option(
            "prefs", {"download.default_directory": save_path})
    # op.add_argument("headless")
    driver = webdriver.Chrome(
        service=Service(
            f"{os.path.realpath(os.path.dirname(__file__))}/chromedriver"),
        options=op)
    driver.get(url)
    s = Slp()
    while True:
        s.empty_cursor()
        try:
            driver.window_handles
        except e.WebDriverException:
            print("dinconnected")
            break


if __name__ == "__main__":
    print(argv)
    if "-h" in argv:
        print("""
yt <url> <-p optional save path>
    -p optional save path otherwise is chrome default
    -u give url
    -h 
""")
    if "-p" in argv:
        i = argv.index("-p")
        path = argv[i+1]
        main(" ".join(argv[1:i]), path)
    else:
        main(" ".join(argv[1:]) if len(argv) > 1 else "")

# needs work
