from django.db import models


class Category(models.Model):
    """Модель категории товаров."""
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование',
        help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание категории',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара."""
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование',
        help_text='Введите название товара'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение',
        help_text='Загрузите изображение товара',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Выберите категорию товара',
        related_name='products',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        help_text='Введите цену товара'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"


class Contact(models.Model):
    """Модель контактной информации."""

    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Введите страну'
    )
    inn = models.CharField(
        max_length=20,
        verbose_name='ИНН',
        help_text='Введите ИНН компании'
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес',
        help_text='Введите адрес'
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Введите email для связи',
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефон',
        help_text='Введите контактный телефон',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"{self.country} - {self.address}"
