from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import get_object_or_404

# def home(request):
#     return render(request, "catalog/product_list.html")


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}) {message}')
#
#     return render(request, "catalog/contacts.html")


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'object': product}
    # context = {'object': Product.objects.get(pk=pk)}
    return render(request, "catalog/product.html", context)

def product_list(request):
    context = {"object_list": Product.objects.all()}
    return render(request, "catalog/product_list.html", context)

