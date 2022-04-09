from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.product_list, name='products'),
]
