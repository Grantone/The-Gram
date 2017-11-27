from django.conf.urls import url, include
from . import views
from django.contrib.auth import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^profile/(?P<username>[-_\w.]+)/followers/$',
        views.followers, name='followers'),
    url(r'^profile/(?P<username>[-_\w.]+)/following/$',
        views.following, name='following'),
    url(r'profile/', views.profile, name='profile'),
]
