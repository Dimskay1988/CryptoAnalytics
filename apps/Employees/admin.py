from django.contrib import admin
from .models import Profile, MessageProfile
# from .forms import ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', "id_telegram", 'email')
    list_filter = ("username", 'id')
    search_fields = ("id_telegram", 'id')
    # # form = ProfileForm


@admin.register(MessageProfile)
class MessageProfileAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'coin', 'currency', 'price', 'created_at', 'tracking_status')
    list_filter = ('coin', 'currency', 'created_at', 'tracking_status')
    search_fields = ('id_profile', 'coin', 'currency', 'created_at', 'tracking_status')
