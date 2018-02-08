from django.urls import re_path

from . import views


urlpatterns = [
    re_path(
        r'^(?P<date>\d{4}-\d{1,2}-\d{1,2})/(?P<locality_id>\d+)/(?:(?P<province_id>\d+)/)?(?:(?P<community_id>\d+)/)?(?:(?P<country_id>\d+)/)?$',
        views.check_public_holiday,
        name='public-holiday',
    ),
]
