from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def check_if_row_in_table_rows(self, row_text):
        items_table = self.browser.find_element(By.ID, 'items_table')
        rows = items_table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ali has heared ablout a cool new online to-do app. He goes to check
        # out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        self.assertEqual(input_box.get_attribute(
            'placeholder'), 'Enter a new to-do item')

        # He types "Read clean-code book" into a text box
        input_box.send_keys('Read clean-code book')
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        # When he hits enter, the pages updates, and now page lists
        # "1: Read clean-code book" as an item in a to-do list
        self.check_if_row_in_table_rows('1: Read clean-code book')

        # There is still a text box inviting him to add another item. He enters
        # "Read TDD with python book" and hits enter
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys('Read TDD with python book')
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        # The page updates again, and now shows both items on his list
        items_table = self.browser.find_element(By.ID, 'items_table')
        rows = items_table.find_elements(By.TAG_NAME, 'tr')
        self.check_if_row_in_table_rows('1: Read clean-code book')
        self.check_if_row_in_table_rows('2: Read TDD with python book')

        # Ali wonders wheater the site will remember her list. Then he sees
        # that the site has generated a unique URL for him and there is some
        # explanations text for that

        # He visits that URL and sees that his to-do list is still there

        # Satisfies, she goes back to sleep
        time.sleep(1)
        self.fail('finish the test')