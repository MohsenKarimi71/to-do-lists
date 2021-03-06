from cgitb import text
from django.forms import ValidationError
from django.test import TestCase
from lists.models import Item, List


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

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text="")
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()