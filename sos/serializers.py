from rest_framework import serializers
from .models import SOSAlert

class SOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOSAlert
        fields = ['id', 'message', 'timestamp']
        read_only_fields = ['timestamp']
