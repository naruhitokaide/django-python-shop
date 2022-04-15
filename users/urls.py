from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='sign-up')
]
