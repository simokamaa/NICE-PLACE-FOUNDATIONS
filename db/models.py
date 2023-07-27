from django.db import models

class login_details(models.Model):
    username = models.CharField(max_length=200),
    password = models.IntegerField()