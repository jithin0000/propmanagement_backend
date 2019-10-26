from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from property.serializers import PropertySerializers, Property, PropImage, PropImageSerializer



class PropertyView(viewsets.ModelViewSet):
    """ view for Property Model """

    serializer_class = PropertySerializers
    queryset = Property.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        state = self.request.GET.get('state')
        prop_type = self.request.GET.get('sale_type')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        order_by = self.request.GET.get('order_by')


        if state is not None:
            state = int(state)
            queryset = queryset.filter(state=state)
        
        if prop_type is not None:
            queryset = queryset.filter(sale_type=prop_type)

        if min_price is not None:
            min_price = int(min_price)
            queryset = queryset.filter(price__gt = min_price)
        
        if max_price is not None:
            max_price = int(max_price)
            queryset = queryset.filter(price__lt = max_price)
        
        if order_by is not None:
            queryset = queryset.order_by(order_by)
        

        return queryset


class PropImageView(viewsets.ModelViewSet):

    """ view for image upload of a property """
    
    serializer_class = PropImageSerializer
    queryset = PropImage.objects.all()

    