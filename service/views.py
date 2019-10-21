from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import Service, ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """ view set for services """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer