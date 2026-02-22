from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ("Role Information", {
            "fields": ("is_patient", "is_caregiver"),
        }),
    )

admin.site.register(User, CustomUserAdmin)
