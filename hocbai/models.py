from __future__ import unicode_literals
from django.db import models
from django import forms
from django.conf import settings
import django.utils.safestring as safestring
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Mucluc(models.Model):
    mucluc1=models.Manager()
    mucluc =  models.CharField('Mục lục', max_length=200)
    noidung = models.TextField('Nội dung')
    date = models.DateField("Ngày:", default=datetime.date.today)
    def __str__(self):
        return self.mucluc
