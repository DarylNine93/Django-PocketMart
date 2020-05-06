from django.urls import path
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete, products_by_category

app_name = "products"

urlpatterns = [
    path('', ProductList.as_view(), name="list"),
    path('add', ProductCreate.as_view(), name="add"),
    path('update/<int:pk>', ProductUpdate.as_view(), name="update"),
    path('delete/<int:pk>', ProductDelete.as_view(), name="delete"),
    path('products-by-category/<int:pk>', products_by_category, name="products_by_category")
]
