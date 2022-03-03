from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Ali goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'new_item_input').send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying 
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, '.has_error').text,
                "The list item can't be empty"
        ))

        # He tries again with some text for the item, which now works
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys("Read a Book!")
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows("1: Read a Book!")

        # Preversely, he now decides to submit a second blank list item
        self.browser.find_element(By.ID, 'new_item_input').send_keys(Keys.ENTER)

        # He recivies a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has_error').text,
            "The list item can't be empty"
        ))
        # And he can correct it by filling some text in
        input_box = self.browser.find_element(By.ID, 'new_item_input')
        input_box.send_keys("Do some workout at home!")
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_table_rows("1: Read a Book!")
        self.wait_for_row_in_table_rows("2: Do some workout at home!")
