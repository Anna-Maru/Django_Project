from django.db import models


class Catalog(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name', unique=True)

    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING, related_name='catalog_group')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    tags = models.TextField(Tag)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
        ordering = ['first_name', 'last_name']
        db_table = 'custom_table_name'

