# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Call(models.Model):
    origin_time = models.DateTimeField(default=None, required = False)
    delay = models.IntegerField(default=0, required = False)
    number = models.CharField(max_length=16, required = True)