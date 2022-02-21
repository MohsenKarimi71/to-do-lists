from django.shortcuts import render, redirect

from .models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('new_item_text', '')
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
    
    items = Item.objects.all()
    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})