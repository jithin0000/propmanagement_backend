from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


from .serializers import CountrySerializer, Country, CitySerializer, City

class CountryViewSet(viewsets.ModelViewSet):
    """ view for country """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    """ view for City """
    queryset = City.objects.all()
    serializer_class = CitySerializer