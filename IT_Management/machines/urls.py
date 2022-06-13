from django.urls import path
from .views import index, machine_01
urlpatterns = [
    path('', index),
    path('machine-01/', machine_01)
]
