from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('Property/', views.list_house),
    path('Register/', views.register, name='register-user-page'),
    path('login/', views.login_view, name='login-page'),
    path('property-register/', views.property_register, name='register-property-page'),
    path('search/', views.search_view, name='search-results-page'),
    path('upload/<int:property_id>', views.upload_view, name='upload-page'),
    path('review/<int:property_id>', views.review_submit, name='review-page'),
    path('logout/', views.logout_view, name='logout-page'),
]
