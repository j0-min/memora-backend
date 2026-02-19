from django.db import models
from accounts.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

