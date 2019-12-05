import os
import unittest
from time import sleep
from selenium import webdriver
os.environ['MOZ_HEADLESS'] = '1'


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        searchbar = self.driver.find_element_by_id('input-search')
        searchbar.send_keys('exotics')
        searchform = self.driver.find_element_by_id('search-form')
        buttons = searchform.find_elements_by_tag_name("button")
        for button in buttons:
            if button.get_attribute('ng-click') == 'search()':
                searchbutton = button
                break
        searchbutton.click()
        sleep(5)
        table = self.driver.find_element_by_id('serverSideDataTable')
        self.assertIn("porsche", table.text.lower())


if __name__ == '__main__':
    unittest.main()
