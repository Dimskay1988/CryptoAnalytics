from django.contrib import admin
from .models import Profile, MessageProfile
from .Forms import ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "id_telegram", "created_at")
    list_filter = ("id", 'username', "created_at")
    search_fields = ("id", "id_telegram", "username", "created_at")
    form = ProfileForm


@admin.register(MessageProfile)
class MessageProfileAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'coin', 'currency', 'price', 'created_at', 'tracking_status')
    list_filter = ('coin', 'currency', 'created_at', 'tracking_status')
    search_fields = ('id_profile', 'coin', 'currency', 'created_at', 'tracking_status')
