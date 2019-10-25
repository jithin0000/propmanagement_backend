from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import Feature , FeatureSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    """ view set for property features """

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    

    def get_queryset(self):
        queryset = super().get_queryset()
        prop = None
        prop = self.request.GET.get('prop')
        if prop == None:
            return queryset
        prop = int(prop)

        return queryset.filter(prop=prop)
