from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

app_name = 'users'

urlpatterns = [
    url(
        r'^signup/$',
        views.signup,
        name='signup',
    ),
    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'users/login.html'},
        name='login',
    ),
]
