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


class Post(TimeStampMixin, SoftDeleteModel):
    class Statuses(models.TextChoices):
        DRAFT = "D", _("Draft")
        PUBLISHED = "P", _("Published")

    title = models.CharField(verbose_name=_("Title"), max_length=124)
    text = models.TextField(verbose_name=_("Body"), help_text=_("Text to display"))
    slug = models.SlugField()
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    status = models.CharField(
        max_length=1,
        choices=Statuses.choices,
        default=Statuses.PUBLISHED,
    )
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=(self.id, self.slug))

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def likes_count(self):
        return self.pvotes.count()

    def user_can_like(self, user):
        user_like = user.uvotes.filter(post=self)
        if user_like.exists():
            return True
        return False


class Image(BaseModel):
    photo = models.FileField(upload_to="posts/images/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")


class Comment(TimeStampMixin, BaseModel):
    text = models.CharField(max_length=128)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    reply_to = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    is_reply = models.BooleanField(default=False)


class Reaction(BaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='uvotes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pvotes')

    def __str__(self):
        return f'{self.user} liked {self.post.slug}'
