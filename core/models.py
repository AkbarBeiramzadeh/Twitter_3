from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet


class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MyManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)

    def archives(self):
        return super().get_queryset().filter(is_deleted=True)


class SoftDeleteModel(BaseModel):
    objects = MyManager()

    is_deleted = models.BooleanField(default=False, db_index=True)

    def delete(self, **kwargs):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
