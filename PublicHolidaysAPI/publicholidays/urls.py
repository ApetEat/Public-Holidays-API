from django.urls import path, re_path, register_converter

from . import converters, views


register_converter(converters.DateConverter, 'yyyymmdd')

urlpatterns = [
    re_path(
        r'^(?P<date>\d{4}[.-/]\d{1,2}[.-/]\d{1,2})/(?P<locality>\d+)/(?:(?P<province>\d+)/)?(?:(?P<community>\d+)/)?(?:(?P<country>\d+)/)?$',
        views.check_public_holiday,
        name='public-holiday',
    ),
]
