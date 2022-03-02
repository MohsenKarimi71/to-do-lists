from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

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
