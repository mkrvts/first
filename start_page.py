import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    """Home page action methods come here"""
    def home_page(self, url):
        return self.driver.get(url)

    def accept_data(self):
        self.driver.switch_to.frame('ufti-iframe')
        self.driver.find_element_by_xpath('//span[contains(text(), "Okej, tack!")]').click()

    def go_to_login_page(self):
        element = self.driver.find_element_by_xpath('//*[@id="top_nav_mypages"]/a')
        element.click()

class LoginPage(BasePage):

    def login(self, username, password):
        us = self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        ps = self.driver.find_element_by_xpath('//*[@id="CredPassword"]').send_keys(password)
        submit = self.driver.find_element_by_xpath('//button[@type="submit"]')
        submit.click()

class UserPage:

    def verify_username(self, username_checker):
        #assert 'username' not in self.driver.page_source
        username_label = self.driver.find_element_by_xpath("//a[@data-trackable='go_to_profile_clicked']")
        assert username_label.text == username_checker
