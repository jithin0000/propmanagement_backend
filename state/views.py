from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import State, StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    """ view set for States of usa """
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset