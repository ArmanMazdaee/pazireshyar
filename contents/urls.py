from django.conf.urls import url
from . import views


app_name = 'contents'
urlpatterns = [
    url(
        r'^university/(?P<pk>[0-9]+)/$',
        views.University.as_view(),
        name='university',
    ),
]
