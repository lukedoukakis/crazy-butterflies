from django.db import models

# Create your models here.

# represents a table
class Testtable(models.Model):
    text = models.CharField(max_length=10)
