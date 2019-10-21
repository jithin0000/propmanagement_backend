from rest_framework import serializers

from .models import Country, City

    
class CountrySerializer(serializers.ModelSerializer):
    """ serializer for country """

    class Meta:
        model = Country
        fields = "__all__"
        


class CitySerializer(serializers.ModelSerializer):
    """ serializer for city """
    # country = CountrySerializer()
    class Meta:
        model = City
        fields ="__all__"