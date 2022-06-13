from django.db import models

class Blood(models.Model):
    blood = models.TextField(max_length=20)
    name = models.TextField(max_length=20)
    phone = models.TextField(max_length=20)
    location = models.TextField(max_length=20)

    class Meta:
        db_table = 'bloodrequest'

class Urgent(models.Model):
    blood = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    location = models.TextField(max_length=100)

    class Meta:
        db_table = 'urgentblood'