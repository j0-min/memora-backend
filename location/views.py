from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Location
from .serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Patient sees own location
        if user.is_patient:
            return Location.objects.filter(user=user)

        # Caregiver sees locations of their patients
        if user.is_caregiver:
            return Location.objects.filter(user__caregiver=user)

        return Location.objects.none()

    def perform_create(self, serializer):
        # Only patients update location
        if self.request.user.is_patient:
            serializer.save(user=self.request.user)
        else:
            raise PermissionError("Only patients can update location.")
