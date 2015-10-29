from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse, reverse_lazy
from allauth.account.adapter import DefaultAccountAdapter  
from .models import Link, Vote, ExtendedUserProfile
from .forms import UserProfileForm, MessageForm

class LinkListView(ListView):
	model = Link
	queryset = Link.with_votes.all()
	paginate_by = 2

class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field =  "username" #key which is used to lookup the model
	template_name = "user_detail.html"

	def get_object(self, queryset=None): # used here for always creating user profle before returning
		user = super(UserProfileDetailView, self).get_object(queryset)
		ExtendedUserProfile.objects.get_or_create(user=user)
		return user

class AccountAdapter(DefaultAccountAdapter):
	def get_login_redirect_url(self, request):
	 	return '/user/'+ request.user.username

class UserProfileEditView(UpdateView):
	model = ExtendedUserProfile
	form_class = UserProfileForm
	template_name = "edit_profile.html"

	#to ensure that a user can not edit someone else's profile
	def get_object(self, queryset=None): 
		return ExtendedUserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("profile", kwargs={'slug': self.request.user})

class MessageCreateView(CreateView):
	model = Link
	form_class = MessageForm

	def form_valid(self, form):
		f = form.save(commit=False)
		f.rank_score = 0.0
		f.started_by = self.request.user
		f.save()
		return super(MessageCreateView, self).form_valid(form)
	
class MessageDetailView(DetailView):
	model = Link

class MessageUpdateView(UpdateView):
	model = Link
	form_class = MessageForm

class MessageDeleteView(DeleteView):
	model = Link
	success_url = reverse_lazy("my_home")