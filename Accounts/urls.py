from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delevery-person/create', views.create_delevery_person, name="create"),
    path('delevery-person/list', views.list_delevery_person, name="list"),
]
