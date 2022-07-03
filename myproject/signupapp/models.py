from django.db import models

class Donors(models.Model):
    fname = models.TextField(max_length=100)
    lname = models.TextField(max_length=100)
    blood = models.TextField(max_length=100)
    aadhaar = models.TextField(max_length=100)
    day = models.TextField(max_length=100)
    month = models.TextField(max_length=100)
    year = models.TextField(max_length=100)
    gender = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    pin = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    cpassword = models.TextField(max_length=100)
    authentication = models.TextField(max_length=50) 

    class Meta:
        db_table = 'donordetails'


class Recipients(models.Model):
    fname = models.TextField(max_length=100)
    lname = models.TextField(max_length=100)
    blood = models.TextField(max_length=100)
    aadhaar = models.TextField(max_length=100)
    day = models.TextField(max_length=100)
    month = models.TextField(max_length=100)
    year = models.TextField(max_length=100)
    gender = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    pin = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    cpassword = models.TextField(max_length=100)
    authentication = models.TextField(max_length=50)

    class Meta:
        db_table = 'recipientdetails'


class Hospitals(models.Model):
    hname = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    pin = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    cpassword = models.TextField(max_length=100)
    authentication = models.TextField(max_length=50)

    class Meta:
        db_table = 'hospitaldetails'




