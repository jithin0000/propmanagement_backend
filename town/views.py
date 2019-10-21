from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import Town, TownSerializer

class TownViewSet(viewsets.ModelViewSet):
    """ view set for town """
    queryset = Town.objects.all()[:10]
    serializer_class = TownSerializer
