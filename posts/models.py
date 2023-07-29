from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import (
    BaseModel,
    SoftDeleteModel,
    TimeStampMixin,
)


# Create your models here.
class Tag(BaseModel):
    text = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.text


