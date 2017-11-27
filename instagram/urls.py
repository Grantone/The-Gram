from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    # url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    # url(r'^profile/(?P<username>[-_\w.]+)/followers/$',
    #     views.followers, name='followers'),
    # url(r'^profile/(?P<username>[-_\w.]+)/following/$',
    #     views.following, name='following'),
    url(r'^profile/', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
