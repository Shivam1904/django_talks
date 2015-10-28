from django.contrib import admin
from .models import Link, Vote, ExtendedUserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
	pass
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vote, VoteAdmin)

# class AdminExtendedUserProfile(admin.ModelAdmin):
# 	pass

class UserProfileInline(admin.StackedInline):
	model = ExtendedUserProfile
	can_delete = False

class AdminExtendedUserProfile(UserAdmin):
	inlines = (UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(),AdminExtendedUserProfile)
