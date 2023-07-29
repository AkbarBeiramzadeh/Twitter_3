from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
    )
    bio = models.CharField(
        verbose_name=_('biography'),
        max_length=100,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='user/images/',
        null=True,
        blank=True,
    )


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings", )
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers", )

    class Meta:
        verbose_name = _("Relation")
        verbose_name_plural = _("Relations")
