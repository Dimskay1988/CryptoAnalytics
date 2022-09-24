from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('id_user', 'name', "password")
        widgets = {'name': forms.TextInput, 'password': forms.TextInput}
