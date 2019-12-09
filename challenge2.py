#import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#os.environ['MOZ_HEADLESS'] = '1'
#http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_challenge2(self):
        self.browser.get("https://www.copart.com")
        searchbar = self.browser.find_element_by_id('input-search')
        searchform = self.browser.find_element_by_id('search-form')
        buttons = searchform.find_elements_by_tag_name("button")
        for button in buttons:
            if button.get_attribute('ng-click') == 'search()':
                searchbutton = button
                break
        searchbar.clear()
        searchbar.send_keys('exotics')
        searchbutton.click()
        wait = WebDriverWait(self.browser, 5)
        table = None
        while not table:
            try:
                table = wait.until(EC.presence_of_element_located((By.ID, 'serverSideDataTable')))
            except TimeoutException:
                searchbar.clear()
                searchbar.send_keys('exotics')
                searchbutton.click()
        tablewait = WebDriverWait(table, 5)
        tablebody = tablewait.until(EC.visibility_of_element_located((By.TAG_NAME,'tbody')))
        self.assertIn("porsche", tablebody.text.lower())


if __name__ == '__main__':
    unittest.main()
