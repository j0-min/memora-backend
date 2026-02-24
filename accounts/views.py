from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import User
from .serializers import RegisterSerializer


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
    username_field = 'email'   # IMPORTANT: tell JWT to use email

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Authenticate using email
        user = authenticate(request=self.context.get("request"),
                            email=email,
                            password=password)

        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        # Generate token
        data = super().validate(attrs)

        # Add extra fields to response
        data['is_patient'] = user.is_patient
        data['is_caregiver'] = user.is_caregiver
        data['email'] = user.email

        return data


# -------------------------
# CUSTOM LOGIN VIEW
# -------------------------

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
