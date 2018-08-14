from rest_framework import serializers

from .models import PublicHoliday


class PublicHolidaySerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    class Meta:
        model = PublicHoliday
        fields = ('date', 'city')


    def get_city(self, obj):
        return obj.city.name