from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name='телефон', null=True)
    date_birth = models.DateField(verbose_name='дата рождения', null=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Comment(models.Model):
    """
    Модель комментария:
    """

    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='автор')
    description = models.TextField(verbose_name='Описание', max_length=1000)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Post(models.Model):

    title = models.CharField(verbose_name='Название', max_length=55)
    text = models.TextField(verbose_name='Описание', max_length=1000)
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='фото')

    author = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, verbose_name='автор')
    comment = models.ManyToManyField(Comment, verbose_name='Комментарий', blank=True, max_length=1000)

    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
