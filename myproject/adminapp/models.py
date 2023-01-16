from django.db import models

class Message(models.Model):
    messages = models.TextField(max_length=200)

class Meta:
    db_table = 'message'


class Donordata(models.Model):
    name = models.TextField(max_length=100)
    blood = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)

class Meta:
    db_table = 'donors_data'


