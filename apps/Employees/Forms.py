from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('id_user', 'name')
        widgets = {'name': forms.TextInput}
