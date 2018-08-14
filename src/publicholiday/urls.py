from django.conf.urls import url

from .views import PublicHolidayRetrieveAPIView


urlpatterns = [
    url(r'^city/(?P<city>[^/]+)/date/(?P<date>[^/]+)/$',
        PublicHolidayRetrieveAPIView.as_view(),
        name='check_public_holiday'),
]