from rest_framework import serializers


from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    '''serializer for Service''' 
    class Meta:
        model = Service 
        fields = '__all__' 