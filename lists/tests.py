from django.test import TestCase

class HomePageTest(TestCase):

    def test_home_page_view_uses_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
        


