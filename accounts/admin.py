from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('email', 'is_patient', 'is_caregiver', 'is_staff')
    list_filter = ('is_patient', 'is_caregiver', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Roles', {'fields': ('is_patient', 'is_caregiver')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_patient', 'is_caregiver', 'is_staff')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
