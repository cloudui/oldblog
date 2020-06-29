from django.contrib import admin

from django.contrib.auth import get_user_model

class CustomUserAdmin(admin.ModelAdmin):
    model = get_user_model()

admin.site.register(get_user_model(), CustomUserAdmin)
