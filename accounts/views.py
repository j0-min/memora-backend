from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims inside JWT token itself
        token['is_patient'] = user.is_patient
        token['is_caregiver'] = user.is_caregiver

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Also include role fields in response body
        data['is_patient'] = self.user.is_patient
        data['is_caregiver'] = self.user.is_caregiver

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
