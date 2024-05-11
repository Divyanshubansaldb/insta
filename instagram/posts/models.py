# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    content = models.CharField(max_length=500)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reaction(models.Model):
    class OPERATION(models.IntegerChoices):
        LIKE = 0, _("like")
        DISLIKE = 1, _("dislike")
        
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "posts.post",
        on_delete=models.CASCADE,
    )
    operation = models.SmallIntegerField(choices=OPERATION.choices)
    
    class Meta:
        unique_together = (('user', 'post'),)
