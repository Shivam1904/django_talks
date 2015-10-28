from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# Create your models here.

class LinkVoteCountManager(models.Manager):
	def get_queryset(self):
		return super(LinkVoteCountManager, self).get_queryset().annotate(
			votes = Count('vote')).order_by("-votes")

class Link(models.Model):
	title = models.CharField("Subject", max_length=100)
	started_by = models.ForeignKey(User)
	started_on = models.DateTimeField(auto_now_add=True)
	rank_score = models.FloatField(default = 0.0)
	url = models.URLField("URL", blank=True)
	description = models.TextField(blank=True)

	with_votes = LinkVoteCountManager()
	objects = models.Manager() # default manager

	def __unicode__(self):
		return self.title

class Vote(models.Model):
	voter = models.ForeignKey(User)
	link = models.ForeignKey(Link)

	def __unicode__(self):
		return 	self.voter.username+" voted "+ self.link.title

class ExtendedUserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	#extra fields
	about_me = models.TextField(null=True)

	def __unicode__(self):
		return "%s's Profile" %self.user

# Signals
def create_profile(sender, instance, created, **kwargs):
	if created :
		profile, create = ExtendedUserProfile.objects.get_or_create(user = instance)
		print profile, create #Shivam's profile True
from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)