from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ali has heared ablout a cool new online to-do app. He goes to check 
        # out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        #self.fail('finish the test')
        
        # He is invited to enter a to-do item straight away

        # He types "Read clean-code book" into a text box

        # When he hits enter, the pages updates, and now page lists
        # "1: Read clean-code book" as an item in a to-do list

        # There is still a text box inviting him to add another item. He enters
        # "Read TDD with python book" and hits enter

        # The page updates again, and now shows both items on his list

        # Ali wonders wheater the site will remember her list. Then he sees 
        # that the site has generated a unique URL for him and there is some 
        # explanations text for that

        # He visits that URL and sees that his to-do list is still there

        # Satisfies, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
    
