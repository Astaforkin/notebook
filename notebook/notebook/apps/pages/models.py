import datetime
from operator import mod
from tabnanny import verbose
from django.db import models
from django.utils import timezone


class Page(models.Model):
    page_title = models.TextField("текст записи")
    pub_date = models.DateTimeField("дата записи")

    def __str__(self):
        return self.page_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now())

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
