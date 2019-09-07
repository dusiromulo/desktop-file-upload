from django.db import models


class User(models.Model):
    username = models.CharField("username", max_length=30)
    password = models.CharField("password", max_length=30)

    def __str__(self):
        return 'Usuário: ' + self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = verbose_name+'s'
