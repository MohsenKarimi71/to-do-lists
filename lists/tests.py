from django.test import TestCase

class HomePageTest(TestCase):

    def test_home_page_view_uses_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'new_item_text': 'Read clean-code book'})
        self.assertTemplateUsed(response, 'lists/home.html')
        self.assertIn('Read clean-code book', response.content.decode())
        


