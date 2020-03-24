from django.urls import path
from .views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete

app_name = "categories"

urlpatterns = [
    path('', CategoryList.as_view(), name="list"),
    path('add', CategoryCreate.as_view(), name="add"),
    path('update/<int:pk>', CategoryUpdate.as_view(), name="update"),
    path('delete/<int:pk>', CategoryDelete.as_view(), name="delete")
]
