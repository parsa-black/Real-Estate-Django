from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('Property/', views.list_house),
    path('Register', views.register, name='register-user-page'),
]
