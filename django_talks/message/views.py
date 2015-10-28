from django.views.generic import ListView, DetailView
from .models import Link, Vote, ExtendedUserProfile
from django.contrib.auth import get_user_model
from allauth.account.adapter import DefaultAccountAdapter

class LinkListView(ListView):
	model = Link
	queryset = Link.with_votes.all()
	paginate_by = 5

class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field =  "username"
	template_name = "user_detail.html"

	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		ExtendedUserProfile.objects.get_or_create(user=user)
		return user

class AccountAdapter(DefaultAccountAdapter):
	def get_login_redirect_url(self, request):
	 	return '/user/'+ request.user.username