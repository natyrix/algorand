from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_account', views.check_account, name='check_account'),
]