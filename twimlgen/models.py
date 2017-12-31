# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Call(models.Model):
    origin_time = models.DateTimeField()
    delay = models.IntegerField(default=0)
    number = models.CharField(max_length=16)