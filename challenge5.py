import os
import unittest
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
os.environ['MOZ_HEADLESS'] = '1'


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_challenge5(self):
        self.browser.get("https://www.copart.com")
        searchbar = self.browser.find_element_by_id('input-search')
        searchform = self.browser.find_element_by_id('search-form')
        buttons = searchform.find_elements_by_tag_name("button")
        for button in buttons:
            if button.get_attribute('ng-click') == 'search()':
                searchbutton = button
                break
        searchbar.clear()
        searchbar.send_keys('porsche')
        searchbutton.click()
        tablelength = None
        wait = WebDriverWait(self.browser, 5)
        while not tablelength:
            try:
                tablelength = wait.until(EC.presence_of_element_located((By.ID, 'serverSideDataTable_length')))
            except TimeoutException:
                searchbar.clear()
                searchbar.send_keys('porsche')
                searchbutton.click()
            finally:
                lengthdropdown = tablelength.find_element_by_tag_name('select')
                lengthdropdown.get_property('2').click()
        table = self.browser.find_element_by_id('serverSideDataTable')
        tableheader = table.find_element_by_tag_name('thead').find_element_by_tag_name('tr')
        for i, column in enumerate(tableheader.find_elements_by_tag_name('th')):
            if column.text == "Model":
                modelcolumn = i
            if column.text == "Damage":
                damagecolumn = i
        tablewait = WebDriverWait(table, 5)
        tablebody = tablewait.until(EC.visibility_of_element_located((By.TAG_NAME,'tbody')))
        rows = tablebody.find_elements_by_tag_name('tr')
        self.assertEqual(len(rows), 100)
        modelset = set()
        damagecounter = Counter()
        DAMAGETYPES = ['REAR END', 'FRONT END', 'MINOR DENT/SCRATCHES', 'UNDERCARRIAGE']
        for row in rows:
            rowdatas = row.find_elements_by_tag_name('td')
            damagecounter[rowdatas[damagecolumn].text] += 1
            modelset.add(rowdatas[modelcolumn].text)
        print("{0} different porsche models".format(len(modelset)))
        print(modelset)
        print(damagecounter)
        for type in DAMAGETYPES:
            print("{0}: {1}".format(type, damagecounter[type]))
            damagecounter[type] = 0
        print("{0}: {1}".format("MISC", sum(damagecounter.values())))


if __name__ == '__main__':
    unittest.main()
