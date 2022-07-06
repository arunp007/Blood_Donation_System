from django.db import models

class Donors(models.Model):
    fname = models.TextField(max_length=50)
    lname = models.TextField(max_length=50)
    blood = models.TextField(max_length=50)
    aadhaar = models.TextField(max_length=50)
    day = models.TextField(max_length=50)
    month = models.TextField(max_length=50)
    year = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    district = models.TextField(max_length=50)
    pin = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)
    authentication = models.TextField(max_length=50)

    class Meta:
        db_table = 'donor_details'


class Recipients(models.Model):
    fname = models.TextField(max_length=50)
    lname = models.TextField(max_length=50)
    blood = models.TextField(max_length=50)
    aadhaar = models.TextField(max_length=50)
    day = models.TextField(max_length=50)
    month = models.TextField(max_length=50)
    year = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    district = models.TextField(max_length=50)
    pin = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)
    authentication = models.TextField(max_length=50)

    class Meta:
        db_table = 'recipient_details'


class Hospitals(models.Model):
    hname = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    location = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    district = models.TextField(max_length=50)
    pin = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    cpassword = models.TextField(max_length=50)
    authentication = models.TextField(max_length=50)

    class Meta:
        db_table = 'hospital_details'

class Admin(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    class Meta:
        db_table = 'admin'

