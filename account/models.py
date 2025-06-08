import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required field.")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')
        if extra_fields.get("is_staff") is not True:
            raise ValueError("admin must be staff.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("admin must be superuser.")
        return self.create_user(email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    USER_TYPE_CHOICES = (
        ("admin", "admin"),
        ("instructor", "instructor"),
        ("client", "client"),

    )
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, help_text="Unique email address used as the username for authentication.")
    user_type = models.CharField(max_length=20, 
                                 choices=USER_TYPE_CHOICES, 
                                 null=True, 
                                 blank=True,   
                                 help_text="Role of the user in the gym (admin, instructor, client).")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
