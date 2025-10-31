from django.db import models
from django.conf import settings
from django.utils import timezone

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    deleted_at= models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        related_name="%(class)s_deleted",
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True

    def soft_delete(self,user=None):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save(update_fields=['deleted_at','is_deleted'])

    def save(self, *args, **kwargs):
        if self.pk:
            if "user" in kwargs:
                self.updated_by = kwargs.pop('user')
        else:
            if "user" in kwargs:
                self.created_by = kwargs.pop('user')
        super().save(*args, **kwargs)



