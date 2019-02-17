from django.urls import path, include
from . import views

urlpatterns = [
    path('style', views.style, name='style'),
]
