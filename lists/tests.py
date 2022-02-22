from urllib import response
from django.test import TestCase
from lists.models import Item, List

class HomePageTest(TestCase):

    def test_view_uses_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


class ListAndItemModelTest(TestCase):
    
    def test_saving_and_retrieving_item_objects(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'This is the first item.'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'This is the second item.'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'This is the first item.')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'This is the second item.')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_view_uses_correct_html(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text="Item number 1", list=list_)
        Item.objects.create(text="Item number 2", list=list_)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'Item number 1')
        self.assertContains(response, 'Item number 2')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new', data={'new_item_text': 'Read clean-code book'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Read clean-code book')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'new_item_text': 'Read clean-code book'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
    