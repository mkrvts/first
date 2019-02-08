import unittest
from selenium import webdriver


class BlocketAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_google(self):
        # step 1 - open home page
        self.driver.get("https:/blocket.se")

        # step 2 - accept data agregation
        self.driver.switch_to.frame('ufti-iframe')
        self.driver.find_element_by_xpath('//span[contains(text(), "Okej, tack!")]').click()

        # step 3 - go to login page
        self.driver.find_element_by_xpath('//*[@id="top_nav_mypages"]/a').click()

        # step 3.1 - step 4 doesn't work without wait
        self.driver.implicitly_wait(5)

        # step 4 - fill in and submit authorization form
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys("krvts.m@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="CredPassword"]').send_keys("qwaszx21")

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        # assert "krvts_m" not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
