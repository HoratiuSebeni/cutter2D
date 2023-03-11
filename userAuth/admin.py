from django.contrib import admin
from .models import UserDetails, ChildUser

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'accountType', 'accountPermisions')

class ChildUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'accountPermisions')

admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(ChildUser, ChildUserAdmin)
