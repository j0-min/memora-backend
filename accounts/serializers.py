from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'is_patient', 'is_caregiver')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_patient=validated_data.get('is_patient', False),
            is_caregiver=validated_data.get('is_caregiver', False),
        )
        return user

