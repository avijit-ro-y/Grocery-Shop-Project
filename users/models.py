from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)