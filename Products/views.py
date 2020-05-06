from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["name", "description", "regular_price", "promotional_price", "weight", "image", "category"]
    template_name = "product_add.html"
    success_url = reverse_lazy("products:list")


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description", "regular_price", "promotional_price", "weight", "image", "category"]
    template_name = "product_update.html"
    success_url = reverse_lazy("products:list")


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("products:list")


@login_required()
def products_by_category(request, pk):
    products = Product.objects.all().filter(category_id=pk)
    return render(request, 'products_by_category.html', {'products': products})
