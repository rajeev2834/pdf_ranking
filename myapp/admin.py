from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, FileData


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',)
        }),
    )
    ordering = ('email',)
    readonly_fields = ('date_joined',)


@admin.register(FileData)
class FileDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'file_name', 'file', 'sde', 'research', 'operations', 'supplychain', 'project', 'data', 'healthcare', 'content', 'marketing', 'teaching', 'security', 'uploaded_at')
    search_fields = ('user', 'file_name', 'file', 'sde', 'research', 'operations', 'supplychain', 'project', 'data', 'healthcare', 'content', 'marketing', 'teaching', 'security', 'uploaded_at')
    fieldsets = (
        (None, {'fields': ('user', 'file_name', 'file', 'sde', 'research', 'operations', 'supplychain', 'project', 'data', 'healthcare', 'content', 'marketing', 'teaching', 'security', 'uploaded_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'file_name', 'file', 'sde', 'research', 'operations', 'supplychain', 'project', 'data', 'healthcare', 'content', 'marketing', 'teaching', 'security', 'uploaded_at')
        }),
    )
    ordering = ('user', 'file_name', 'file', 'sde', 'research', 'operations', 'supplychain', 'project', 'data', 'healthcare', 'content', 'marketing', 'teaching', 'security', 'uploaded_at')
    readonly_fields = ('uploaded_at',)