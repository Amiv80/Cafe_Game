from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "vip_member", "date_add"]
    list_filter = ["vip_member"]


admin.site.register(Member, MemberAdmin)
