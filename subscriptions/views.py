from django.http import JsonResponse, Http404
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

def getRecord(classObject, pk):
    try:
        return classObject.objects.get(pk=pk)
    except:
        raise Http404

# Create your views here.
class Businesses(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Business,BusinessSerializer)
        
    def post(self,request):
        return createNewRecord(request, BusinessSerializer)

class BusinessRecord(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        business = getRecord(Business, pk)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        record = getRecord(Business,pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Offerings(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Business_Offering,BusinessOfferingSerializer)
    
    def post(self,request):
        return createNewRecord(request, BusinessOfferingSerializer)

class OfferingRecord(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        offering = getRecord(Business_Offering, pk)
        serializer = BusinessOfferingSerializer(offering)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        record = getRecord(Business_Offering,pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Customers(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Customer,CustomerSerializer)
    
    def post(self,request):
        return createNewRecord(request, CustomerSerializer)

class CustomerRecord(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        customer = getRecord(Customer, pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        record = getRecord(Customer,pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Orders(APIView):  
    permission_classes = [AllowAny]
    def get(self,request):
        return getAllRecords(Order, OrderSerializer)
    
    def post(self,request):
        return createNewRecord(request, OrderSerializer)
    
class OrderRecord(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        order = getRecord(Order, pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        record = getRecord(Order,pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
