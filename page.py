import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    """Home page action methods come here"""
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

class UserPage(BasePage):

    def verify_username(self, username_checker):
        #assert 'username' not in self.driver.page_source
        username_label = self.driver.find_element_by_xpath("//a[@data-trackable='go_to_profile_clicked']")
        assert username_label.text == username_checker

    def navigate_to_messages(self):
        self.driver.find_element_by_xpath('//*[@class="blocket-icon blocket-icon-chat"]').click()

class MessagesPage(BasePage):

    def get_list_of_messages(self):
        messages_list = self.driver.find_elements_by_xpath('//*[@class="conversation-list__item__message__delete__icon blocket-icon blocket-icon-trash"]')
        message_ids_list = self.driver.find_elements_by_xpath('//a[@class="conversation-list__item pas border-bottom"]')
        conversation_list = self.driver.find_elements_by_xpath('//*[@class="conversation-list__item__picture"]')
        return messages_list, message_ids_list, conversation_list

    def delete_message(self, messages_list, conversation_list, message_index):
        if len(messages_list) < message_index:
            print('The list of messages is less than the number of message to delete')
        else:
            element_to_hover_over = conversation_list[message_index-1]
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            element_to_delete = messages_list[message_index - 1].click()
            self.driver.find_element_by_xpath('//button[contains(text(), "Ja, ta bort")]').click()
            # self.driver.find_element_by_xpath('//button[contains(text(), "Avbryt")]').click()

    def verify_that_message_deleted(self, message_ids, message_index):
        element = self.driver.find_elements_by_partial_link_text(str(message_ids[message_index-1]))
        assert not element