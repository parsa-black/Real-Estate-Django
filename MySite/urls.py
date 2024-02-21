from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('Register/', views.register, name='register-user-page'),
    path('login/', views.login_view, name='login-page'),
    path('property-register/', views.property_register, name='register-property-page'),
    path('property/', views.property_view, name='property-page'),
    path('property/<int:property_id>', views.single_property, name='single-property-page'),
    path('upload/<int:property_id>', views.upload_view, name='upload-page'),
    path('search/', views.search_view, name='search-results-page'),
    path('review/<int:property_id>', views.review_submit, name='review-register-page'),
    path('logout/', views.logout_view, name='logout-page'),
    path('services', views.services, name='services-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='contact-page')
]
