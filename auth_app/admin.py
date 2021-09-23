from django.contrib import admin
from .models import Profile

# Customizing model fields shown in the default Admin Panel
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'customer_phone_number']

admin.site.register(Profile, ProfileAdmin)  
