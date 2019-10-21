from rest_framework.serializers import ModelSerializer

from .models import Feature

class FeatureSerializer(ModelSerializer):
    """ serializer for features """

    class Meta:
        model = Feature
        fields = "__all__"