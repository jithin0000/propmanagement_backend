from rest_framework import serializers


from .models import Town

class TownSerializer(serializers.ModelSerializer):
    '''serializer for Town''' 
    class Meta:
        model = Town 
        fields = '__all__' 