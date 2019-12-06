import os
import unittest
from selenium import webdriver
os.environ['MOZ_HEADLESS'] = '1'


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_challenge1(self):
        self.browser.get("https://www.copart.com")
        popular = self.browser.find_element_by_id('tabTrending')
        for a in popular.find_elements_by_tag_name('a'):
            href = a.get_attribute('href')
            if "category" not in href:
                print(a.text + ' - ' + href)


if __name__ == '__main__':
    unittest.main()
