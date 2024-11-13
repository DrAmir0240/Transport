# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        create new user
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        full_name = self.full_name(full_name)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)  # hashed password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        """
        create superuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, full_name, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # admin access

    USERNAME_FIELD = 'email'  # email as userID
    REQUIRED_FIELDS = []  # just email and password for creating user

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} {self.email}"


class MainManager(CustomUser):
    access_code = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    grand_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"name:{self.full_name}, access-code:{self.access_code}, balance:{self.grand_balance}"


class Manager(CustomUser):
    employee_id = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='manager_pictures')
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    management_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"name:{self.full_name}, management-date:{self.management_date}, balance:{self.balance}, employee:{self.employee_id}"


class Driver(CustomUser):
    drive_license_id = models.CharField(max_length=255, unique=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='driver_pictures')
    debt_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    travel_count = models.IntegerField(default=0)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"name:{self.full_name}, debt balance:{self.debt_balance}"


class Customer(CustomUser):
    social_security_number = models.IntegerField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='customer_pictures')
    business_field = models.CharField(max_length=255, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"name:{self.full_name}, wallet-balance:{self.wallet_balance}"
