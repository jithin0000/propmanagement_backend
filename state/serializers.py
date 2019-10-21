from rest_framework import serializers


from .models import State

class StateSerializer(serializers.ModelSerializer):
    '''serializer for State''' 
    class Meta:
        model = State 
        fields = '__all__' 