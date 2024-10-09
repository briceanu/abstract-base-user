# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomBaseManager  
import uuid

class BlogUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_married = models.BooleanField(default=False)
    signup_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)
    """
    is_active and is_staff are needed when creating a superuser
    """
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  

    objects = CustomBaseManager()  # Assign the custom manager

    # USERNAME_FIELD is used as at he unique identifier for authentication purposes
    USERNAME_FIELD = 'username'
      # Fields required when creating a superuser
    # REQUIRED_FIELDS = ['username']

    @property
    def id(self):
        return self.user_id
