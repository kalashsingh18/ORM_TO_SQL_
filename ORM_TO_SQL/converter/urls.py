from django.contrib import admin
from django.urls import path, include
from .views import check,mainconverter

urlpatterns = [
	path('', check, name='test'),
    path('mainconverter/',mainconverter , name='mainconverter'),
]
