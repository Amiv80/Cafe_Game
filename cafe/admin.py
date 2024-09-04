from django.contrib import admin
from .models import Member
from django.apps import apps

if not admin.site.is_registered(Member):
    @admin.register(Member)
    class MemberAdmin(admin.ModelAdmin):
        list_display = ('name', 'vip_member', 'date_add')
        search_fields = ('name',)
