from django.db import models

# Create your models here.

class send_command(models.Model):
    trxid = models.CharField(max_length=100)
    command = models.CharField(max_length=20)
    topic = models.CharField(max_length=20)
    message = models.JSONField()