from django.contrib import admin
from .models import Profile
from .Forms import ProfileForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "id_user", "name", "surname")
    list_filter = ("id", 'name', "surname")
    search_fields = ("id", "id_user", "name", "surname")
    form = ProfileForm

