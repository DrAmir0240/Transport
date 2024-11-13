from django.contrib import admin

from Users.models import CustomUser, MainManager, Manager, Driver, Customer, CustomerImage, DriverImage, ManagerImage


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)


@admin.register(MainManager)
class MainManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'access_code', 'grand_balance')
    search_fields = ('access_code', 'full_name')
    ordering = ('full_name',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee_id', 'balance', 'management_date')
    search_fields = ('employee_id', 'full_name')
    ordering = ('full_name',)


@admin.register(ManagerImage)
class ManagerImageAdmin(admin.ModelAdmin):
    list_display = ('manager_assigned', 'image', 'uploaded_at')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'drive_license_id', 'debt_balance', 'rate')
    search_fields = ('drive_license_id', 'full_name')
    ordering = ('full_name',)


@admin.register(DriverImage)
class DriverImageAdmin(admin.ModelAdmin):
    list_display = ('driver', 'image', 'uploaded_at')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'social_security_number', 'wallet_balance')
    search_fields = ('social_security_number', 'full_name')
    ordering = ('full_name',)


@admin.register(CustomerImage)
class CustomerImageAdmin(admin.ModelAdmin):
    list_display = ('customer', 'image', 'uploaded_at')
