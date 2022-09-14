from email import message
from django.db import models

class Contact(models.Model):
    name = models.TextField(max_length=25)
    email = models.TextField(max_length=25)
    message = models.TextField(max_length=50)

    class Meta:
        db_table = 'contact_data'