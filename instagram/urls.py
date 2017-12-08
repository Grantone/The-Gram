from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/', views.update_user_profile, name="updateuserprofile"),
    url(r'^upload/new_post', views.new_post, name="new_post"),
    url(r'^like/$', views.add_like, name='like'),
    url(r'^profile/upvote/(\d+)$', views.upvote_post, name="upvote_post"),
    url(r'^post/downvote/(\d+)$', views.downvote_post, name="downvote_post")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
