from rest_framework import serializers 

from property.models import Property, PropImage


class PropertySerializers(serializers.ModelSerializer):

    """ serializer for property """
    class Meta:
        model = Property
        fields = "__all__"


class PropImageSerializer(serializers.ModelSerializer):

    """ serializer for property image """

    class Meta:
        model = PropImage
        fields = ('prop', 'prop_image_url')