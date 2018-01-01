# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Call(models.Model):
    delay = models.IntegerField(default=0)
    number = models.CharField(max_length=16)

class Game(models.Model):
    call = models.OneToOneField(Call, default=None)
    fizzbuzz = models.IntegerField(default=0)