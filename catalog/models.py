from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(upload_to='images', verbose_name="изображение", **NULLABLE)
    price = models.PositiveIntegerField(verbose_name="цена за штуку")
    created_at = models.DateField(verbose_name="Дата создания", auto_now=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)
    # manufactured_at = models.DateField(verbose_name="Дата производства продукта", auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория",
                                 **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name="Продукт")
    version_number = models.PositiveIntegerField(verbose_name="Номер версии")
    version_title = models.CharField(max_length=150, verbose_name="Название вервии")
    is_actual = models.BooleanField(default=True, verbose_name="Актуальная")

    def __str__(self):
        return f'{self.version_title} {self.version_number}'

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"

