from rest_framework import serializers
from .models import *


class GreenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenType
        fields = '__all__'


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayCollection
        fields = '__all__'


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerBouquet
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'


class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosOrder
        fields = ['bouquet', 'order', 'count', 'discount']


class PosSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PosSupply
        fields = ['green', 'supply', 'count']
