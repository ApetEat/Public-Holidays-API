from django.urls import path, register_converter

from . import converters, views

# Create your urls here.

register_converter(converters.DateConverter, 'yyyymmdd')

urlpatterns = [
    path(
        '<yyyymmdd:date>/<str:community>/<str:province>/<str:locality>/',
        views.check_is_public_holiday,
        name='public-holidays',
    ),
]
