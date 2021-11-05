from django.contrib import admin

from simple_auth.models import CustomAuthUser


@admin.register(CustomAuthUser)
class CustomAuthUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active')
    list_display_links = ("username",)
    search_fields = ("username",)

