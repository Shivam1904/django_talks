from django import forms
from .models import ExtendedUserProfile

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = ExtendedUserProfile
		exclude = ("user",)
