from rest_framework import serializers
from GDA.product.models import GroceryDetails

class GrocerySerializer(serializers.ModelSerializer):    
    class Meta:
        model = GroceryDetails
        fields = ('product_name','brand','catogery_id','price','available_qty')

class GroceryListSerializer(serializers.ModelSerializer):
    file_name = serializers.CharField()
    catogery = serializers.CharField()
    status = serializers.CharField()
    class Meta:
        model = GroceryDetails
        fields = ('product_id','file_name','product_name','brand','catogery','price','available_qty','status')