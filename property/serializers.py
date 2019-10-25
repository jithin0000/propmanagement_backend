from rest_framework import serializers 

from property.models import Property, PropImage
from agent.serializers import AgentSerializer

class PropertySerializers(serializers.ModelSerializer):

    agent = AgentSerializer()

    """ serializer for property """
    class Meta:
        model = Property
        fields = "__all__"


class PropImageSerializer(serializers.ModelSerializer):

    """ serializer for property image """

    class Meta:
        model = PropImage
        fields = ('prop', 'prop_image_url')