from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('id_user', 'name', "surname")
        widgets = {'name': forms.TextInput, 'surname': forms.TextInput}