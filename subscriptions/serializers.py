from rest_framework import serializers
from .models import Business, Business_Offering, Customer, Order
from rest_framework.validators import UniqueValidator

class BusinessSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[UniqueValidator(queryset=Business.objects.all())])

    def create(self, validated_data):
        return Business.objects.create(**validated_data)
    
    def validate(self, data):
        if Business.objects.filter(name=data['name']).count() > 1:
            raise serializers.ValidationError("Business record already exists")
        return data

class BusinessOfferingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    business = serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())

    def create(self, validated_data):
        return Business_Offering.objects.create(**validated_data)
    
    def validate(self, data):
        try:
            business = Business.objects.get(name = data["business"])
        except:
            raise serializers.ValidationError("Business id provided not associated with business record")
        if Business_Offering.objects.filter(name=data['name'], business = business).count() > 1:
            raise serializers.ValidationError("Business offering record already exists")
        return data

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[UniqueValidator(queryset=Customer.objects.all())])

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    offer = serializers.PrimaryKeyRelatedField(queryset=Business_Offering.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    business = serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    def validate(self, data):
        invalid_fields = []
        try:
            business = Business.objects.get(name = data["business"])
        except:
            invalid_fields.append('business')
        try:
            customer = Customer.objects.get(name = data["customer"])
        except:
            invalid_fields.append('customer')
        try:
            offer = Business_Offering.objects.get(name = data["offer"], business = business)
        except:
            invalid_fields.append('offer')
        if(len(invalid_fields) > 0):
            print(invalid_fields)
            raise serializers.ValidationError(f"Invalid fields provided: {' '.join([field for field in invalid_fields]) }")
        if Order.objects.filter(offer=offer, business = business, customer=customer).count() > 1:
            print('exists already!')
            raise serializers.ValidationError("Business offering record already exists")
        return data
