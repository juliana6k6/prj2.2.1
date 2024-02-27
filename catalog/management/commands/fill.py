from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.db import connection
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удалите все продукты
        # Удалите все категории
        Category.objects.all().delete()
        Product.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        category_list = [
            {'name': 'Собачий корм'},
            {'name': 'Кошачий корм'},
            {'name': 'Корм для попугаев'}]

        product_list = [
            {"name": "pedigree",
             "category": 1,
             "price": 4,
             },
            {"name": "kitekat",
             "category": 2,
             "price": 3,
             },
            {"name": "chappie",
             "category": 1,
             "price": 6,
             },
            {"name": "trio",
             "category": 3,
             "price": 2,
             }]

        # Обходим все значения категорий из списка для получения информации об одном объекте
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item))
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        print(Category.objects)
        # Обходим все значения продуктов из списка для получения информации об одном объекте
        for product_item in product_list:
            pk = product_item["category"]
            category = Category.objects.filter(pk=pk)
            price1 = product_item["price"]
            name1 = product_item["name"]
            product_for_create.append(
                Product(name=name1,
                        price=price1,
                        сategory=category))
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
