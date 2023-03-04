from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'accountType', 'accountPermisions')

admin.site.register(UserDetails, UserDetailsAdmin)

