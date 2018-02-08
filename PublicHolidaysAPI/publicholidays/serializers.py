from rest_framework import serializers

# Create your serializers here.


class PublicHolidaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicHolidayCalendar
        fields = ('id', 'date', 'country', 'community', 'province', 'locality')
