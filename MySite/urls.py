from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.homepage, name='home-page'),
    path('Property/', views.list_house),
    path('Register', views.register, name='Register User'),
]
