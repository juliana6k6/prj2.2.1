from django.urls import path
from catalog.views import product_list
from catalog.views import contacts
from catalog.views import product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="product_list"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>", product, name="product"),
]