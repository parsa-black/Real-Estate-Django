from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('Property/', views.list_house),
    path('Register/', views.register, name='register-user-page'),
    path('login/', views.login_view, name='login-page'),
    path('property-register/', views.property_register, name='register-property-page'),
]
