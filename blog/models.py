from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name="слаг", blank=True, null=True)
    body = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to='new_images', verbose_name="изображение", blank=True, null=True)
    created_at = models.DateField(verbose_name="Дата создания", auto_now=True)
    published = models.BooleanField(default=True, verbose_name="Опубликован")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Счётчик просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"
from django.db import models

# Create your models here.
