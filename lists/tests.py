from django.test import TestCase
from lists.models import Item

class HomePageTest(TestCase):

    def test_home_page_view_uses_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'new_item_text': 'Read clean-code book'})
        
        self.assertTemplateUsed(response, 'lists/home.html')
        self.assertIn('Read clean-code book', response.content.decode())
        

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_item_objects(self):
        first_item = Item()
        first_item.text = 'This is the first item.'
        first_item.save()

        second_item = Item()
        second_item.text = 'This is the second item.'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'This is the first item.')
        self.assertEqual(second_saved_item.text, 'This is the second item.')
