from django.shortcuts import render
from catalog.models import Product, Version
# from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

# def home(request):
#     return render(request, "catalog/product_list.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')

    return render(request, "catalog/contacts.html")

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        actual_versions = versions.filter(is_actual=True)
        if actual_versions:
            product.actual_version_title = actual_versions.first().version_title
            product.actual_version_number = actual_versions.first().version_number
        else:
            product.actual_version_title = 'Нет актуальной версии'
            product.actual_version_number = "Нет номера актуальной версии"

        context_data['object'] = product
        return context_data

# def product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'object': product}
#     # context = {'object': Product.objects.get(pk=pk)}
#     return render(request, "catalog/product.html", context)

# def product_list(request):
#     context = {"object_list": Product.objects.all()}
#     return render(request, "catalog/product_list.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            actual_versions = versions.filter(is_actual=True)
            if actual_versions:
                product.actual_version = actual_versions.first()
            else:
                product.actual_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
