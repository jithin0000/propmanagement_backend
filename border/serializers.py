from rest_framework import serializers 



from .models import Border

class BorderSerializer(serializers.ModelSerializer):
    '''serializer for Border''' 
    class Meta:
        model = Border 
        fields = '__all__' 