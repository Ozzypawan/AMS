from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Rank(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10, unique=True)
    designation = models.CharField(max_length=255)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default='M')
    address = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document')
    citizenship_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField()
    issued_district = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=10, unique=True)
    pan_upload = models.ImageField(upload_to='documents/pan/', blank=True, null=True)
    citizenship_upload = models.ImageField(upload_to='documents/citizenship/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Document"

class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bank_name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=30, unique=True)
    bank_account_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} Bank Details"

class Device(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    device_id = models.CharField(max_length=50, unique=True)
    fingerprint_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.user.username} Device"
