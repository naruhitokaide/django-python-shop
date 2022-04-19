from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/add', views.add_cart, name='add-to-cart')
]
