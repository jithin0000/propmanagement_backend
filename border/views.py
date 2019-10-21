from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BorderSerializer, Border

class BorderViewSet(viewsets.ModelViewSet):
    """ view set for border """

    queryset = Border.objects.all()[:10]
    serializer_class = BorderSerializer