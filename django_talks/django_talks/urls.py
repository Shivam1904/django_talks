from django.conf.urls import include, url
from django.contrib import admin
from message.views import LinkListView, UserProfileDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', LinkListView.as_view(), name='my_home'),
    url(r'^user/(?P<slug>\w+)/', UserProfileDetailView.as_view(), name="profile"),
]
	