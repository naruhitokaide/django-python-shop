from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.cart, name='basket_add'),
    path('mycart', views.cart_list, name='cart_list'),
    path('add', views.cart_remove, name='remove'),
]