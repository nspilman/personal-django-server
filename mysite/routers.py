from rest_framework import routers
from weddingPlanning.viewsets import HotelViewSet

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet)