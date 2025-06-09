from django.contrib import admin
from account.models import CustomUser
# Register your models here.


# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', "email", "full_name"]
    search_fields = ['first_name', 'last_name', 'email']


    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

