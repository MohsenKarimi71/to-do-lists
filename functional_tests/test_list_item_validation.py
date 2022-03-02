from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Ali goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying 
        # that list items cannot be blank

        # He tries again with some text for the item, which now works

        # Preversely, he now decides to submit a second blank list item

        # He recivies a similar warning on the list page

        # And he can correct it by filling some text in
        self.fail('Write me!')