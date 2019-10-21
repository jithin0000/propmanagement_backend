from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CImagesSerializer, CImages, Agent, AgentSerializer


class CImageViewSet(viewsets.ModelViewSet):
    """ view set for image upload of agent """
    queryset = CImages.objects.all()
    serializer_class = CImagesSerializer


class AgentViewset(viewsets.ModelViewSet):
    """ view set for agent """

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer