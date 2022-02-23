from django.test import LiveServerTestCase

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def wait_for_row_in_table_rows(self, row_text):
        start_time = time.time()
        while True:
            try:
                items_table = self.browser.find_element(By.ID, 'items_table')
                rows = items_table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
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

        # When he hits enter, the pages updates, and now page lists
        # "1: Read clean-code book" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows('1: Read clean-code book')

        # There is still a text box inviting him to add another item. He enters
        # "Read TDD with python book" and hits enter
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys('Read TDD with python book')
        input_box.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.wait_for_row_in_table_rows('1: Read clean-code book')
        self.wait_for_row_in_table_rows('2: Read TDD with python book')
        # Satisfied, she goes back to sleep
    
    def test_multiple_users_can_start_lists_on_defferent_urls(self):
        # Ali starts a new to-do list
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys('Read TDD with python book')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows('1: Read TDD with python book')

        # He notices that her list has a unique URL
        ali_list_url = self.browser.current_url
        self.assertRegex(ali_list_url, '/lists/.+')

        # Now a new user, Reza, comes along to the site.
        # we use a new browser session to make sure that no information
        # of Ali's is coming through cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Reza visits the home page. There is no sign of Ali's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Read TDD with python book', page_text)
        self.assertNotIn('clean-code', page_text)

        # Reza starts a new list by entering a new item.
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows('1: Buy milk')

        # Reza gets his own unique URL
        reza_list_url = self.browser.current_url
        self.assertRegex(reza_list_url, '/lists/.+')
        self.assertNotEqual(reza_list_url, ali_list_url)

        # Again, there is no trace of Ali's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Read TDD with python book', page_text)
        self.assertIn('Buy milk', page_text)
        # satisfied, they both go back to sleep

    def test_layout_and_styling(self):
        width = 1024
        height = 768
        # Ali goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(width, height)

        # He noticed that the input box is nicely centered
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            width / 2,
            delta=10 
        )

        # He starts a new list and sees the input in nicely centered
        # there too
        input_box.send_keys('testing item')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows('1: testing item')
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            width / 2,
            delta=10 
        )
