from rest_framework import serializers, fields

class OrderSerializer(serializers.Serializer):
    """Order Serializer"""
    order_id = fields.UUIDField()
    total = fields.DecimalField(decimal_places=2, max_digits=15)
