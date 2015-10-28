from django import forms
from .models import ExtendedUserProfile, Link

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = ExtendedUserProfile
		exclude = ("user",)

class MessageForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ("started_by","rank_score",)
