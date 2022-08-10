from operator import mod
from django.db import models

class Page(models.Model):
    page_title = models.TextField('текст записи')
    pub_date = models.DateTimeField('дата записи')

