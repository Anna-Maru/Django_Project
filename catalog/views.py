from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    return render(request, 'index.html')

def show_data(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def submit_data(request):
    request.GET
    request.POST
    if request.method == 'POST':
        return HttpResponse("Данные отправлены")

def show_item(request, item_id):
    return render(request, 'app/item.html', {'item_id': item_id})
