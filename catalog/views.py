from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    """Главная страница"""
    return render(request, 'home.html')


def contacts(request):
    """Страница контактов с формой обратной связи"""
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print('=' * 50)
        print('Получена форма обратной связи')
        print('=' * 50)
        print(f'Имя: {name}')
        print(f'Сообщение: {message}')
        print('=' * 50)
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'contacts.html')
