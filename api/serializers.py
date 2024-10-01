from rest_framework import serializers

class SerialNumberSerializer(serializers.Serializer):
    serialNumber = serializers.ListField(
        child=serializers.CharField(max_length=10)
    )
