from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth
from message.views import LinkListView, UserProfileDetailView, UserProfileEditView

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', LinkListView.as_view(), name='my_home'),
    url(r'^user/(?P<slug>\w+)/', UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
]
	