from django.urls import path
from . import views

urlpatterns = [
    path('Property', views.list_house),
]
