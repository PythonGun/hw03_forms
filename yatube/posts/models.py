from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_empty_field

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Укажите заголовок поста'
    )

    slug = models.SlugField(
        unique=True,
        null=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        help_text='Сделайте описание'
    )

    def __str__(self):
        return self.title


class Post(models.Model):

    text = models.TextField(
        validators=[validate_empty_field],
        verbose_name='Текст поста',
        help_text='Укажите текст поста'
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Укажите дату публикации'
    )

    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
        help_text='Укажите автора поста'
    )

    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Укажите группу'
    )

    class Meta:
        ordering = ['-pub_date']

        def __str__(self):
            return self.text[:15]
