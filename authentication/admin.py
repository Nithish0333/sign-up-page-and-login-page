from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Display columns in the user list
    list_display = ['username', 'email', 'fullname', 'is_staff', 'is_active', 'date_joined', 'last_login']
    
    # Filter options in the sidebar
    list_filter = ['is_staff', 'is_active', 'is_superuser', 'date_joined']
    
    # Search fields
    search_fields = ['username', 'email', 'fullname', 'first_name', 'last_name']
    
    # Fields to display when editing a user
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('fullname',)}),
    )
    
    # Fields to display when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('fullname', 'email')}),
    )
    
    # Ordering
    ordering = ['-date_joined']
    
    # Actions
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        """Make selected users active"""
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} user(s) marked as active.')
    make_active.short_description = "Mark selected users as active"
    
    def make_inactive(self, request, queryset):
        """Make selected users inactive"""
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} user(s) marked as inactive.')
    make_inactive.short_description = "Mark selected users as inactive"


