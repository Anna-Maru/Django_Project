from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу данных'

    def add_arguments(self, parser):
        """Добавление аргументов командной строки."""
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед загрузкой'
        )

    def handle(self, *args, **options):
        """Основная логика команды."""

        if options['clear']:
            self.stdout.write(self.style.WARNING('Удаление существующих данных...'))
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✓ Данные удалены'))

        self.stdout.write(self.style.MIGRATE_HEADING('\nСоздание категорий...'))

        categories_data = [
            {
                'name': 'Электроника',
                'description': 'Электронные устройства и аксессуары для дома и офиса'
            },
            {
                'name': 'Одежда',
                'description': 'Модная одежда для мужчин и женщин'
            },
            {
                'name': 'Книги',
                'description': 'Художественная и техническая литература'
            },
            {
                'name': 'Спорт и отдых',
                'description': 'Товары для спорта и активного отдыха'
            },
            {
                'name': 'Дом и сад',
                'description': 'Товары для дома, дачи и сада'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(**cat_data)
            categories[cat_data['name']] = category
            status = '✓' if created else '→'
            self.stdout.write(
                self.style.SUCCESS(f'{status} Категория: {category.name}')
            )


        self.stdout.write(self.style.MIGRATE_HEADING('\nСоздание продуктов...'))

        products_data = [
            {
                'name': 'Ноутбук ASUS VivoBook',
                'description': 'Мощный ноутбук с процессором Intel Core i5, 8GB RAM, SSD 256GB',
                'category': categories['Электроника'],
                'price': Decimal('69999.00')
            },
            {
                'name': 'Смартфон Samsung Galaxy A54',
                'description': 'Современный смартфон с отличной камерой 50MP и батареей 5000 mAh',
                'category': categories['Электроника'],
                'price': Decimal('42000.00')
            },
            {
                'name': 'Наушники Sony WH-1000XM4',
                'description': 'Беспроводные наушники с активным шумоподавлением',
                'category': categories['Электроника'],
                'price': Decimal('25000.00')
            },
            {
                'name': 'Планшет iPad Air',
                'description': 'Планшет Apple с экраном Retina 10.9 дюймов',
                'category': categories['Электроника'],
                'price': Decimal('55000.00')
            },
            {
                'name': 'Умные часы Apple Watch',
                'description': 'Умные часы с GPS и мониторингом здоровья',
                'category': categories['Электроника'],
                'price': Decimal('35000.00')
            },
            {
                'name': 'Футболка Nike Dri-FIT',
                'description': 'Спортивная футболка из качественного дышащего материала',
                'category': categories['Одежда'],
                'price': Decimal('2500.00')
            },
            {
                'name': 'Джинсы Levis 501',
                'description': 'Классические джинсы синего цвета, прямой крой',
                'category': categories['Одежда'],
                'price': Decimal('5500.00')
            },
            {
                'name': 'Кроссовки Adidas Ultraboost',
                'description': 'Удобные беговые кроссовки с технологией Boost',
                'category': categories['Одежда'],
                'price': Decimal('12000.00')
            },
            {
                'name': 'Куртка Columbia',
                'description': 'Зимняя куртка с утеплителем',
                'category': categories['Одежда'],
                'price': Decimal('8500.00')
            },
            {
                'name': 'Python для начинающих',
                'description': 'Практическое руководство по программированию на Python',
                'category': categories['Книги'],
                'price': Decimal('1200.00')
            },
            {
                'name': 'Чистый код',
                'description': 'Роберт Мартин - создание, анализ и рефакторинг кода',
                'category': categories['Книги'],
                'price': Decimal('1800.00')
            },
            {
                'name': 'Алгоритмы. Построение и анализ',
                'description': 'Классический учебник по алгоритмам',
                'category': categories['Книги'],
                'price': Decimal('2500.00')
            },
            {
                'name': 'Гантели разборные 2x10 кг',
                'description': 'Набор разборных гантелей для домашних тренировок',
                'category': categories['Спорт и отдых'],
                'price': Decimal('3000.00')
            },
            {
                'name': 'Йога-мат Premium',
                'description': 'Коврик для йоги из экологичного материала, 183x61 см',
                'category': categories['Спорт и отдых'],
                'price': Decimal('2200.00')
            },
            {
                'name': 'Велосипед горный',
                'description': 'Горный велосипед с 21 скоростью',
                'category': categories['Спорт и отдых'],
                'price': Decimal('28000.00')
            }
        ]

        for prod_data in products_data:
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults=prod_data
            )
            status = '✓' if created else '→'
            self.stdout.write(
                self.style.SUCCESS(
                    f'{status} Продукт: {product.name} - {product.price} руб.'
                )
            )

        # Статистика
        self.stdout.write(self.style.MIGRATE_HEADING('\n' + '=' * 60))
        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Загрузка завершена!'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'  Категорий: {Category.objects.count()}'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'  Продуктов: {Product.objects.count()}'
            )
        )
        self.stdout.write(self.style.MIGRATE_HEADING('=' * 60))
