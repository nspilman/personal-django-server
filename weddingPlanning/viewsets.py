from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) # specify the permission class in your view
