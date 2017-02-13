from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
    url('^signup/$', views.signup, name='signup'),
    url('^login/$', views.login),
]
