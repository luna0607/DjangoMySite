# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
