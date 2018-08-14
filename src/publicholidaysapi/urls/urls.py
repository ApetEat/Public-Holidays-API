from django.conf.urls import include, url


urlpatterns = [
    url('v1/public-holiday/', include('publicholiday.urls')),
]