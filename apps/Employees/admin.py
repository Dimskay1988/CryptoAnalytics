from django.contrib import admin
from .models import Profile, Message
from .Forms import ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "id_user", "name")
    list_filter = ("id", 'name')
    search_fields = ("id", "id_user", "name")
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "text", "created_at")
    list_filter = ("id", 'created_at')
