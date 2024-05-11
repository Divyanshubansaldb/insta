from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    mobile_no = models.BigIntegerField()
