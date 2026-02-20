from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SOSAlert, SMSLog
from .serializers import SOSSerializer


class SOSViewSet(viewsets.ModelViewSet):
    serializer_class = SOSSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Patient sees own SOS
        if user.is_patient:
            return SOSAlert.objects.filter(user=user)

        # Caregiver sees SOS of their patients
        if user.is_caregiver:
            return SOSAlert.objects.filter(user__caregiver=user)

        return SOSAlert.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_patient:
            raise PermissionError("Only patients can trigger SOS.")

        sos = serializer.save(user=user)

        # Simulated SMS
        if user.caregiver:
            message_body = (
                f"🚨 MEMORA SOS ALERT 🚨\n"
                f"Patient: {user.username}\n"
                f"Message: {sos.message}\n"
                f"Time: {sos.timestamp}"
            )

            # Save SMS log
            SMSLog.objects.create(
                recipient=user.caregiver.username,
                message=message_body
            )

            print("\n==============================")
            print("📲 SIMULATED SMS SENT")
            print(message_body)
            print("==============================\n")
