from django.db import models

class Message(models.Model):
    messages = models.TextField(max_length=200)

class Meta:
    db_table = 'message'
