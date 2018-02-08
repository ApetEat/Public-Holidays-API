from django.urls import path, re_path, register_converter

from . import converters, views

# Create your urls here.


register_converter(converters.DateConverter, 'yyyymmdd')

urlpatterns = [
    path(
        '<yyyymmdd:date>/<int:locality>/<int:province>/<int:community>/<int:country>',
        views.check_public_holiday,
        name='public-holiday',
    ),
    re_path(
        r'(?P<date>\d{4}/\d{1,2}/\d{1,2})/(?P<locality>\d+)/(?:/(?P<province>\d+))?/(?:/(?P<community>\d+))?/(?:/(?P<country>\d+))?/',
        views.check_public_holiday,
        name='re-public-holiday',
    ),
]
