from django.contrib import admin
from catalog.models import Category, Product, Version

# Register your models here.
# @admin.register(Имя_модели)python manage.py
# class Имя_МоделиAdmin(admin.ModelAdmin):
#     list_display = (список_полей_модели_для_отображения)
#     list_filter = (список_полей_для_фильтрации)
#     search_fields = (список_полей_для_поиска)
# Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id,
# название, цену и категорию.
# При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории,
# а также осуществлять поиск по названию и полю описания.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'version_number', 'product', 'is_actual')
    list_filter = ('is_actual',)


