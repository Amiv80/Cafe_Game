from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'vip_member', 'date_add')
    search_fields = ('name',)


admin.site.register(Member, MemberAdmin)