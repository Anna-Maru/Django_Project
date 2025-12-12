from django.db import models


class Catalog(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
        ordering = ['first_name', 'last_name']
        db_table = 'custom_table_name'

