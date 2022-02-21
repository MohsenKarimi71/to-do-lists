from django.shortcuts import render, redirect

from .models import Item

# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['new_item_text'])
    return redirect('/lists/the-only-list-in-the-world/')