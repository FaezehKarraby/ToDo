import os
from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TodoTest(LiveServerTestCase):
    def testform(self):
        path = os.path.dirname(os.path.abspath(__file__))
        address = os.path.join(path, 'chromedriver')
        browser = webdriver.Chrome(address)
        browser.get('http://127.0.0.1:8000/account/login/')
        sleep(2)
        username = browser.find_element_by_xpath('//*[@id="id_username"]')
        username.send_keys('admin')
        password = browser.find_element_by_xpath('//*[@id="id_password"]')
        password.send_keys('adminadmin')
        sleep(2)
        button = browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/button')
        button.send_keys(Keys.ENTER)
        sleep(2)

        browser.get('http://127.0.0.1:8000/')
        subject = browser.find_element_by_xpath('//*[@id="id_subject"]')
        subject.send_keys('p2')
        description = browser.find_element_by_xpath('//*[@id="id_description"]')
        description.send_keys('projct2 \n deadline : 2 days.')
        sleep(2)
        button = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/form/center/input')
        button.send_keys(Keys.ENTER)
        sleep(2)

        subject = browser.find_element_by_xpath('//*[@id="id_subject"]')
        subject.send_keys('p3')
        description = browser.find_element_by_xpath('//*[@id="id_description"]')
        description.send_keys('projct3 \n deadline : 2 days.')
        sleep(2)
        button = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/form/center/input')
        button.send_keys(Keys.ENTER)
        sleep(2)

        button = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div/form/button')
        button.send_keys(Keys.ENTER)
        sleep(5)
