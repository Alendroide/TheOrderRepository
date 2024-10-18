from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
@admin.register(Employee)
class Employer(BaseUserAdmin):
    pass