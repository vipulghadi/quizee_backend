from django.contrib import admin
from django.urls import path
from ..views.client import CurrentUserAPIView

urlpatterns = [
    path('me/', CurrentUserAPIView.as_view()),
]
