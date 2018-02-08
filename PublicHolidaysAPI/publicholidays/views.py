from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PublicHolidaySerializer
from .models import PublicHolidayCalendar


@api_view(['GET'])
def check_public_holiday(request, **kwargs):
    """
    Check if date is public holiday for given locality.
    """
    params = {}
    for key, value in kwargs.items():
        if value is not None:
            params[key] = value

    try:
        public_holiday = PublicHolidayCalendar.objects.get(**params)
    except PublicHolidayCalendar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PublicHolidaySerializer(public_holiday)
    return Response(serializer.data, status=status.HTTP_200_OK)
