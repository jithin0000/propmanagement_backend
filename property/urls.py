from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PropertyView, PropImageView
from place.views import  CountryViewSet, CityViewSet
from feature.views import FeatureViewSet
from service.views import ServiceViewSet
from agent.views import CImageViewSet, AgentViewset

from town.views import TownViewSet
from border.views import BorderViewSet
from state.views import StateViewSet

router = DefaultRouter()

router.register('property', PropertyView, base_name="property")
router.register('image', PropImageView, base_name="property_image")
router.register('border', BorderViewSet, base_name="country")
router.register('state', StateViewSet, base_name="state")
router.register('features', FeatureViewSet, base_name="property_features")
router.register('service', ServiceViewSet, base_name="serice")

router.register('agent', AgentViewset, base_name="agent")
router.register('agent_image', CImageViewSet, base_name="agent_image")


urlpatterns = [
    path('', include(router.urls))
]