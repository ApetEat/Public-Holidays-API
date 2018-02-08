from django.urls import re_path

from . import views


urlpatterns = [
    re_path(
        r'^(?P<date>\d{4}-\d{1,2}-\d{1,2})/'
        r'(?P<locality_id>\d+)/'
        r'(?:(?P<province_id>\d+)/)?'
        r'(?:(?P<community_id>\d+)/)?'
        r'(?:(?P<country_id>\d+)/)?$',
        views.check_public_holiday,
        name='public-holiday',
    ),
]
