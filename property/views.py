from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from property.serializers import PropertySerializers, Property, PropImage, PropImageSerializer



class PropertyView(viewsets.ModelViewSet):
    """ view for Property Model """

    serializer_class = PropertySerializers
    queryset = Property.objects.all()

    def get_queryset(self):
        print(self.request.GET)
        queryset = super().get_queryset()
        queryset = queryset
        return queryset


class PropImageView(viewsets.ModelViewSet):

    """ view for image upload of a property """
    
    serializer_class = PropImageSerializer
    queryset = PropImage.objects.all()

    