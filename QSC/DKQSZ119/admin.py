from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, WorkerInfo, AttendanceRecord, Z119group

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'z119group', 'is_leader', 'is_director']
    fieldsets = UserAdmin.fieldsets + (
        ('Thông tin thêm', {'fields': ('z119group', 'is_leader', 'is_director')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(WorkerInfo)
admin.site.register(AttendanceRecord)
admin.site.register(Z119group)