import unittest
from selenium import webdriver
import page

class DeleteMessages(unittest.TestCase):
    username = 'krvts.m@gmail.com'
    password = 'qwaszx21'
    starting_url = "https:/blocket.se"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.starting_url)
        self.home_page = page.HomePage(self.driver)
        self.home_page.accept_data()
        self.home_page.go_to_login_page()
        login_page = page.LoginPage(self.driver)
        login_page.login(self.username, self.password)

    def test_auth_method(self):
        username_checker = 'krvts_m'
        user_page = page.UserPage(self.driver)
        user_page.verify_username(username_checker)


    ''' This test deletes the 2nd message for the list of Blocket messages'''
    def test_message_deleting(self):
        # index_of_message_to_delele starts form 1
        index_of_message_to_delete = 2
        user_page = page.UserPage(self.driver)
        user_page.navigate_to_messages()
        messages_page = page.MessagesPage(self.driver)
        messages_list, message_ids_list, converastions_list = messages_page.get_list_of_messages()
        #messages_page.delete_message(messages_list, converastions_list, index_of_message_to_delete)
        messages_page.verify_that_message_deleted(message_ids_list, index_of_message_to_delete)

    #

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()