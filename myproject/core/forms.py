from django import forms
from .models import Profile


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('user', 'location', 'birthdate', 'role')
