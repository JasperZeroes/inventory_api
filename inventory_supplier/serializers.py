from rest_framework import serializers
from .models import Item, Supplier

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Name is required')
        return value

class SupplierSerializer(serializers.ModelSerializer):
    items_supplied = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True, required=False)

    class Meta:
        model = Supplier
        fields = "__all__"

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Name is required')
        return value

    def validate_contact_info(self, value):
        if not value:
            raise serializers.ValidationError('Contact info is required')
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items_supplied', [])
        supplier = Supplier.objects.create(**validated_data)
        supplier.items_supplied.set(items_data)
        return supplier

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items_supplied', [])
        instance.name = validated_data.get('name', instance.name)
        instance.contact_info = validated_data.get('contact_info', instance.contact_info)
        instance.save()
        instance.items_supplied.set(items_data)
        return instance

class SupplierDetailSerializer(serializers.ModelSerializer):
    items_supplied = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ['supplier_id', 'name', 'contact_info', 'items_supplied']
