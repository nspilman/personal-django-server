from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Business, Business_Offering, Customer, Order
import datetime
from .serializers import BusinessSerializer, BusinessOfferingSerializer, CustomerSerializer, OrderSerializer

def getAllRecords(classObject, Serializer):
    records = classObject.objects.all()
    serializer = Serializer(records, many=True)
    return Response(serializer.data)

def createNewRecord(request, Serializer):
    data = JSONParser().parse(request)
    serializer = Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# Create your views here.
class Businesses(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Business,BusinessSerializer)
        
    def post(self,request):
        return createNewRecord(request, BusinessSerializer)

class Offerings(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Business_Offering,BusinessOfferingSerializer)
    
    def post(self,request):
        return createNewRecord(request, BusinessOfferingSerializer)

class Customers(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Customer,CustomerSerializer)
    
    def post(self,request):
        return createNewRecord(request, CustomerSerializer)

class Orders(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Order, OrderSerializer)
    
    def post(self,request):
        return createNewRecord(request, OrderSerializer)
