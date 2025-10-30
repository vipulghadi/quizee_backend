from django.contrib import admin
from django.urls import path
from ..views.admin import AdminLoginView

urlpatterns = [
    path('admin-login/', AdminLoginView.as_view()),
]
