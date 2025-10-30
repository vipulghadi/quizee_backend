from django.contrib import admin
from django.urls import path
from ..views.client import TestAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
]
