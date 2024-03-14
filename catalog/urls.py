from django.urls import path
# from catalog.views import product_list
# from catalog.views import product
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
