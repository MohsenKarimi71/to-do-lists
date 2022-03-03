from typing import List
from django.forms import ValidationError
from django.shortcuts import render, redirect

from .models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['new_item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error_msg = "The list item can't be empty"
        return render(request, 'lists/home.html', {"error": error_msg})
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(
        text=request.POST['new_item_text'],
        list=list_
    )
    return redirect(f'/lists/{list_.id}/')