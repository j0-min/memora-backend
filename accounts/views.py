from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

User = get_user_model()


# -------------------------
# REGISTER VIEW
# -------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# -------------------------
# CUSTOM JWT SERIALIZER
# -------------------------

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = 'email'   # use email as login field

    def validate(self, attrs):
        # Map email → username internally for JWT
        attrs['username'] = attrs.get('email')

        data = super().validate(attrs)

        # Add extra fields
        data['is_patient'] = self.user.is_patient
        data['is_caregiver'] = self.user.is_caregiver
        data['email'] = self.user.email

        return data


# -------------------------
# CUSTOM LOGIN VIEW
# -------------------------

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
