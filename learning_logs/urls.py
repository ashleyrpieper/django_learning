"""Defines URL patterns for learning_logs."""

from django.url import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]