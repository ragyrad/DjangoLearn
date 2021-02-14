from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
