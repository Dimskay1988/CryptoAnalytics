from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "token"]
    list_display = ("username", "email", "token")
    list_filter = ("id", 'username', "email")
    search_fields = ("id", "username", "email")
