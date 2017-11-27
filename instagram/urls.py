from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
