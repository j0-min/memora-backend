
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Patient sees own reminders
        if user.is_patient:
            return Reminder.objects.filter(user=user)

        # Caregiver sees reminders of their patients
        if user.is_caregiver:
            return Reminder.objects.filter(user__caregiver=user)

        return Reminder.objects.none()

    def perform_create(self, serializer):
        # Only patients can create reminders
        if self.request.user.is_patient:
            serializer.save(user=self.request.user)
        else:
            raise PermissionError("Only patients can create reminders.")
