from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import Feature , FeatureSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    """ view set for property features """

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
