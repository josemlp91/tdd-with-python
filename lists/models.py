from django.db import models

# Create your models here.

class Item(models.Model):
    text = models.CharField(max_length=512, null=True)