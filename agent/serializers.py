from rest_framework import serializers

from .models import CImages, Agent


class CImagesSerializer(serializers.ModelSerializer):
    '''serializer for CImages''' 
    class Meta:
        model = CImages 
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    '''serializer for Agent''' 
    class Meta:
        model = Agent 
        fields = '__all__' 