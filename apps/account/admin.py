from django.contrib import admin
from apps.account.models import UserModel

admin.site.register(UserModel)

admin.site.site_header = "Quizee Admin"
admin.site.site_title = "Quizee Portal"
admin.site.index_title = "Welcome to Quizee Dashboard"