
import re
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from seleniumwire.utils import decode

from fake_useragent import UserAgent
from termcolor import cprint
import essentials
import platform
import sys
import os
import brotli
import json
import requests

API_LIST = {
    'pokeapi': 'https://pokeapi.co/api/v2/pokemon/1',
    'dragonballapi': 'https://dragon-ball-api.herokuapp.com/documentation',
    'test': 'https://postman-echo.com/'

}


global_log = essentials.Logger()


def message(typeMessage, text):
    if typeMessage == "info":
        global_log.info(text)
        cprint(text, "green")
    elif typeMessage == "warning":
        global_log.warning(text)
        cprint(text, "yellow")
    elif typeMessage == "error":
        global_log.error(text)
        cprint(text, "red")


# Create a session
def CreateSession():
    message("info", "Open chromedriver")
    options = Options()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')

    if platform.system() == "Windows":
        message("warning", "Selenium run on Windows")
        chrome_path = './drivers/chromedriver96.exe'
    elif platform.system() == "Darwin":
        message("warning", "Selenium run on Mac OS")
        chrome_path = './drivers/chromedriver98'
    else:
        message("error", "Missing chromedriver")
        sys.exit()
    try:
        ser = Service(chrome_path)
        driver = webdriver.Chrome(options=options, service=ser)
        return driver
    except Exception as e:
        message("error", e)
        sys.exit()


def POSTRequestAPI(session, url, sessid, arg):
    # TODO POSTRequest
    cprint("POST REQUEST METHOD", 'green')
    print(url, arg)
    res = requests.post(url, data=arg)
    print(res.text)


def PUTRequestAPI(session, url, sessid, arg):
    # TODO PUTRequest
    cprint("PUT REQUEST METHOD", 'green')
    res = requests.put(url, data=arg)
    print(res.text)


def PATCHRequestAPI(session, url, sessid, arg):
    # TODO PATCHRequest
    cprint("PATCH REQUEST METHOD", 'green')
    res = requests.patch(url, data=arg)
    print(res.text)


def DELETERequestAPI(session, url, sessid, arg):
    # TODO DELETERequest
    cprint("DELETE REQUEST METHOD", 'green')
    res = requests.delete(url, data=arg)
    print(res.text)


def GETRequestAPI(session, url, sessid, arg):
    # TODO GETRequest
    session.get(API_LIST['pokeapi'])
    for request in session.requests:
        if request.response:
            print(request.url,
                  request.response.status_code,
                  request.response.headers['Content-Type'])

            resp = request.response.body
            resp = brotli.decompress(resp).decode("utf-8")
            resp = json.loads(resp)
            print(json.dumps(resp, indent=2))


def main():
    s = CreateSession()
    if s == None:
        return False

    arg = dict()
    GETRequestAPI(s, API_LIST['pokeapi'], '', arg)

    arg = dict()
    arg['name'] = 'ABC',
    arg['email'] = 'xyz@gmail.com'
    POSTRequestAPI(s, API_LIST['test']+'post', '', arg)

    PUTRequestAPI(s, API_LIST['test']+'put', '', arg)

    PATCHRequestAPI(s, API_LIST['test']+'patch', '', 'testing patch')

    DELETERequestAPI(s, API_LIST['test']+'delete', '', 'testing delete')


if __name__ == '__main__':
    main()
