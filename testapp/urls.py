from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_fun, name='my_fun')
]