from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delivery-person/create', views.create_delivery_person, name="create"),
    path('delivery-person/list', views.list_delivery_person, name="list"),
    path('delivery-person/profile', views.delivery_person_profile, name="profile"),
    path('delivery-person/profile-edit', views.delivery_person_profile_edit, name="profile-edit"),
]
