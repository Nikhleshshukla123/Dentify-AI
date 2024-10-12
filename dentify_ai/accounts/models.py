from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.core.validators import EmailValidator
from accounts.helpers import validators as v
import datetime as dt


class User(AbstractUser):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('x', 'Other')
    )
    username = None
    # profile data
    email = models.EmailField(unique=True, validators=[EmailValidator, v.validate_email])
    phone = models.CharField(max_length=10, unique=True, validators=[v.validate_phone])
    first_name = models.CharField(max_length=150, validators=[v.validate_first_name])
    last_name = models.CharField(max_length=150, blank=True, validators=[v.validate_last_name])
    gender = models.CharField(max_length=10, blank=True, choices=GENDER)
    dob = models.DateField(blank=True, null=True)
    profile_pic = models.FileField(upload_to='media/user/profile', null=True, blank=True)
    last_modified = models.DateField(auto_now=True)
    # verification detail
    verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6,blank=True, null=True)
    email_otp_ts = models.DateTimeField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    phone_otp = models.CharField(max_length=6,blank=True, null=True)
    phone_otp_ts = models.DateTimeField(blank=True, null=True)
    phone_verified_at = models.DateTimeField(blank=True, null=True)
    # forgot password
    fget_otp = models.CharField(max_length=6,blank=True, null=True)
    fget_token = models.CharField(max_length=100, null=True, blank=True)
    fget_otp_ts = models.DateTimeField(blank=True, null=True)
    last_fget = models.DateTimeField(blank=True, null=True)
    # suspension
    suspended = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name']

    
    class Meta:
        db_table = "Users"
        verbose_name = "User"

    def __str__(self):
        return f'{self.email} : {self.first_name}'
