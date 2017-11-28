from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^profile/', views.profile, name='profile'),
    url('^profiles/edit', views.update_user_profile, name="updateuserprofile"),
    url(r'^upload/new_post', views.new_post, name="new_post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
