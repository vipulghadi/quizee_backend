from django.contrib import admin
from django.urls import path
from ..views.admin import UploadQuestionMaterialAPIView

urlpatterns = [
    path('upload-material/', UploadQuestionMaterialAPIView.as_view()),
]
