from django.db import models

class Blood(models.Model):
    blood = models.TextField(max_length=20)
    name = models.TextField(max_length=20)
    phone = models.TextField(max_length=20)
    location = models.TextField(max_length=20)

    class Meta:
        db_table = 'hospitalbloodrequest'
