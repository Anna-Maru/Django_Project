from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalog.models import Product, Contact


def home(request):
    """Главная страница с последними продуктами"""
    products_list = Product.objects.all().order_by('-created_at')


    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)


    latest_products = products_list[:5]
    print("\n" + "=" * 60)
    print("ПОСЛЕДНИЕ 5 ПРОДУКТОВ:")
    print("=" * 60)
    for i, product in enumerate(latest_products, 1):
        print(f"{i}. {product.name} - {product.price} руб.")
        print(f"   Категория: {product.category.name if product.category else 'Без категории'}")
        print(f"   Создан: {product.created_at.strftime('%d.%m.%Y %H:%M')}")
        print("-" * 60)

    context = {
        'products': products,
        'page_obj': products,
    }
    return render(request, 'catalog/home.html', context)


def product_detail(request, pk):
    """Страница с подробной информацией о товаре."""
    product = get_object_or_404(Product, pk=pk)


    print("\n" + "=" * 60)
    print(f"ПРОСМОТР ТОВАРА: {product.name}")
    print("=" * 60)
    print(f"ID: {product.pk}")
    print(f"Цена: {product.price} руб.")
    print(f"Категория: {product.category.name if product.category else 'Без категории'}")
    print("=" * 60)

    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    """Страница контактов с информацией из БД."""
    contact_info = Contact.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print('=' * 50)
        print('Получена форма обратной связи')
        print('=' * 50)
        print(f'Имя: {name}')
        print(f'Телефон: {phone}')
        print(f'Сообщение: {message}')
        print('=' * 50)

    context = {
        'contact': contact_info
    }
    return render(request, 'catalog/contacts.html', context)
