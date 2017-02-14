from django.conf.urls import url
from . import views


app_name = 'contents'
urlpatterns = [
    url(
        r'^university/(?P<pk>[0-9]+)/$',
        views.University.as_view(),
        name='university',
    ),
    url(
        r'^universities/$',
        views.universities,
        name='universities',
    ),
    url(
        r'^field/(?P<pk>[0-9]+)/$',
        views.Field.as_view(),
        name='field',
    ),
    url(
        r'^fields/$',
        views.fields,
        name='fields',
    ),
    url(
        r'^program/(?P<pk>[0-9]+)/$',
        views.Program.as_view(),
        name='program',
    ),
    url(
        r'^programs/$',
        views.programs,
        name='programs',
    ),
]
