from django.urls import path, include
from . import views

# Define a list of url patterns

urlpatterns = [
    path('', views.index),
]

