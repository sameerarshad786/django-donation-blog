from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_verified', 'is_staff', 'created_at', 'updated_at']
    list_editable = ['is_verified', 'is_staff']
    list_filter = ['is_verified', 'is_staff']

admin.site.register(User, UserAdmin)
