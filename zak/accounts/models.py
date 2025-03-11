from django.db import models
from django.contrib.auth.models import User



class Id(models.Model):
    name = models.CharField('Название игры', max_length=25)
    number = models.FloatField('Айди игры', max_length=30, primary_key=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Айдишник'
        verbose_name_plural = 'Айдишники'

class Steam(models.Model):
    gameclub = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    login = models.CharField('Логин', max_length=25, primary_key=True, serialize=False)
    password = models.CharField('Пароль', max_length=25)
    secret_key = models.CharField('Cекретный ключ', max_length=30)
    status = models.BooleanField('Статус аккаунта', default=0)
    game_list = models.ManyToManyField(Id, blank=True, related_name='games')

    def __str__(self):
        return self.login
    class Meta:
        verbose_name = 'Steam'
        verbose_name_plural = 'Steam'

class Epic(models.Model):
    login = models.CharField('Логин', max_length=25)
    password = models.CharField('Пароль', max_length=25)
    secret_key = models.CharField('секретный ключ', max_length=30)
    status = models.BooleanField('Статус аккаунта', default=0)
    gamename = models.CharField('Игры на аккаунте', max_length=15)

    def __str__(self):
        return self.login
    class Meta:
        verbose_name = 'Epic'
        verbose_name_plural = 'Epic'



# Create your models here.
