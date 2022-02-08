from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html', {
        'new_item_text': request.POST.get('new_item_text')
    })