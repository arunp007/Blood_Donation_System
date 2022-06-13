from django.db import models

class Camps(models.Model):
    camp = models.TextField(max_length=100)
    date = models.DateTimeField(max_length=100)
    address = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)

    class Meta:
        db_table = 'camps'
