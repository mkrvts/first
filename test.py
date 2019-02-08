import unittest
from selenium import webdriver

class BlocketAuthorization(unittest.TestCase):

    # creating instance
    def setUp(self):
        self.driver = webdriver.Chrome()

    def blocket_authorization(self):
        driver = self.driver

        # step 1 - open home page
        driver.get("https:/blocket.se")

        # step 2 - accept data agregation
        driver.switch_to.frame('ufti-iframe')
        accept_data_tracking = driver.find_element_by_xpath('//span[contains(text(), "Okej, tack!")]').click()

        # step 3 - go to login page
        login_page_link = driver.find_element_by_xpath('//*[@id="top_nav_mypages"]/a').click()

        # step 3.1 - step 4 doesn't work without wait
        driver.implicitly_wait(5)

        # step 4 - fill in and submit authorization form
        email_field = driver.find_element_by_xpath('//input[@type="email"]').send_keys("krvts.m@gmail.com")
        password_field = driver.find_element_by_xpath('//*[@id="CredPassword"]').send_keys("qwaszx21")

        login_button = driver.find_element_by_xpath('//button[@type="submit"]').click()

        assert "krvts_m" not in driver.page_source

    def tearDoun(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()