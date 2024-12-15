from django.contrib import admin
from .models import Account


# Register your models here.
@admin.register(Account)
class AdminManager(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "user_image",
        "date_joined",
        "is_admin",
    ]
    search_fields = [
        "username",
        "email"
    ]