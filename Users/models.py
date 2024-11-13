from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        create new user
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
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
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    def has_perm(self, perm, obj=None):
        # This method checks if the user has the specified permission
        # Typically, this will interact with the `Permission` model
        return self.is_superuser

    def has_module_perms(self, app_label):
        # This method checks if the user has permission to access a particular app
        return self.is_superuser


class MainManager(CustomUser):
    access_code = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    grand_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - Access Code: {self.access_code}, Balance: {self.grand_balance}"


class Manager(CustomUser):
    employee_id = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='manager_pictures', blank=True, null=True)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    management_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - Employee ID: {self.employee_id}, Balance: {self.balance}"


class ManagerImage(models.Model):
    manager_assigned = models.ForeignKey(Manager, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='manager_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.manager.full_name}"

class Driver(CustomUser):
    drive_license_id = models.CharField(max_length=255, unique=True)
    assigned_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='drivers')
    picture = models.ImageField(upload_to='driver_pictures', blank=True, null=True)
    debt_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    travel_count = models.IntegerField(default=0)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - License ID: {self.drive_license_id}, Debt: {self.debt_balance}"

class DriverImage(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='driver_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.driver.full_name}"

class Customer(CustomUser):
    social_security_number = models.CharField(max_length=255, unique=True)
    business_field = models.CharField(max_length=255, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.full_name} - SSN: {self.social_security_number}, Wallet: {self.wallet_balance}"

class CustomerImage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='customer_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.customer.full_name}"
