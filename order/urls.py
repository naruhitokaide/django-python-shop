from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/add', views.cart, name='add-to-cart')
]