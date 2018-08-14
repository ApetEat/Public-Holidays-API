from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer

from django.shortcuts import get_object_or_404

from .serializers import PublicHolidaySerializer
from .models import PublicHoliday


class PublicHolidayRetrieveAPIView(RetrieveAPIView):
    """
    Check if a day is a public holiday in a city
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = PublicHolidaySerializer
    permission_classes = ()

    def get_object(self):
        return get_object_or_404(PublicHoliday,
                                 city__name=self.kwargs.get('city').lower(),
                                 date=self.kwargs.get('date'))