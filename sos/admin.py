from django.contrib import admin
from .models import SOSAlert, SMSLog

admin.site.register(SOSAlert)
admin.site.register(SMSLog)
