from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='sign-up'),
    path('logout', views.logout_view , name='logout')
]
