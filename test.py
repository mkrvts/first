import unittest
from selenium import webdriver


class BlocketAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    # Next task:
    # Create a new test:
    # a. Login to your account
    # b. Navigate to messages
    # c. Delete 'second' message from message history
    # d. Verify that it's deleted
    # Additional conditions:
    # 1. Consider reusing of test data (username and password) by using variables
    # 2. Create a new class for each page.
    # 3. Class should contain methods of user interaction with page and reuse locators (e.g. MainPage.login(username, password) )


    def test_google(self):
        # step 1 - open home page
        self.driver.get("https:/blocket.se")

        # step 2 - accept data agregation
        self.driver.switch_to.frame('ufti-iframe')
        self.driver.find_element_by_xpath('//span[contains(text(), "Okej, tack!")]').click()

        # step 3 - go to login page
        self.driver.find_element_by_xpath('//*[@id="top_nav_mypages"]/a').click()

        # step 4 - fill in and submit authorization form
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys("krvts.m@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="CredPassword"]').send_keys("qwaszx21")

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        #assert "krvts_m" not in self.driver.page_source
        username_label = self.driver.find_element_by_xpath("//a[@data-trackable='go_to_profile_clicked']")
        assert username_label.text == "krvts_m"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
