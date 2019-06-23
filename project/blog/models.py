from django.db import models


class Message(models.Model):
    text = models.TextField(verbose_name=u'Сообщение', max_length=2000)
    time = models.DateTimeField(verbose_name=u'Дата сообщения', auto_now_add=True)
