from django.conf.urls import url
from django.contrib.auth import views as auth_views

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
    url(
        r'^logout/$',
        auth_views.logout_then_login,
        name='logout',
    ),
    url(
        r'^$',
        views.Profile.as_view(),
        name='profile',
    )
]
