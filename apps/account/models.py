import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import transaction
from django.db import models
from django.utils import timezone

from apps.core.enums import RoleEnum


class UserManager(BaseUserManager):
    def _create_user(self, email, password, phone_number, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not phone_number:
            raise ValueError("User must have a phone number")

        email = self.normalize_email(email)

        with transaction.atomic():
            user = self.model(
                email=email,
                phone_number=phone_number,
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, email, password, phone_number, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, phone_number **extra_fields)

    def create_superuser(self, email, password, phone_number, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, phone_number, **extra_fields)



class UserModel(AbstractBaseUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField( max_length=255,null=True,blank=True)
    last_name = models.CharField( max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=254,unique=True)
    phone_number = models.CharField( max_length=20,null=True,blank=True)
    role=models.CharField( max_length=50,choices=RoleEnum.choices(),default=RoleEnum.USER)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    objects=UserManager()

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
        indexes = [
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.email





