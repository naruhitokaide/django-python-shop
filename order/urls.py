from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.cart, name='basket_add'),
]