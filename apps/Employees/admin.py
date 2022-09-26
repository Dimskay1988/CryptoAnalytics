from django.contrib import admin
from .models import Profile, MessageProfile
# from .forms import ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ("id_telegram")
    # list_filter = ("id_telegram")
    # search_fields = ("id_telegram")
    # # form = ProfileForm


@admin.register(MessageProfile)
class MessageProfileAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'coin', 'currency', 'price', 'created_at', 'tracking_status')
    list_filter = ('coin', 'currency', 'created_at', 'tracking_status')
    search_fields = ('id_profile', 'coin', 'currency', 'created_at', 'tracking_status')
