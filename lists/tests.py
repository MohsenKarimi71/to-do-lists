from urllib import response
from django.test import TestCase
from lists.models import Item

class HomePageTest(TestCase):

    def test_view_uses_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'new_item_text': 'Read clean-code book'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Read clean-code book')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'new_item_text': 'Read clean-code book'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
    
    def test_saves_only_on_POST_requests(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

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


class ListViewTest(TestCase):

    def test_view_uses_correct_html(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_items(self):
        Item.objects.create(text="Item number 1")
        Item.objects.create(text="Item number 2")

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'Item number 1')
        self.assertContains(response, 'Item number 2')
        