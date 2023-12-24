from django.urls import path
from . import views

urlpatterns = [
    path('Property', views.hello_world),
]
