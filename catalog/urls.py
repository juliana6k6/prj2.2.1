from django.urls import path
from catalog.views import product_list
from catalog.views import product
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="product_list"),
    path("product/<int:pk>", product, name="product_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
