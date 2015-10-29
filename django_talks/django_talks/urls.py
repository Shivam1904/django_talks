from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth

from message.views import LinkListView, UserProfileDetailView, UserProfileEditView
from message.views import MessageCreateView, MessageDetailView
from message.views import MessageUpdateView, MessageDeleteView

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', LinkListView.as_view(), name='my_home'),
    url(r'^user/(?P<slug>\w+)/', UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^message/(?P<pk>\d+)$', (MessageDetailView.as_view()), name="message_detail"),
    url(r'^message/create/$', auth(MessageCreateView.as_view()), name="message_create"),
    url(r'^message/update/(?P<pk>\d+)/$', auth(MessageUpdateView.as_view()), name="message_update"),
    url(r'^message/delete/(?P<pk>\d+)/$', auth(MessageDeleteView.as_view()), name="message_delete"),
]
	