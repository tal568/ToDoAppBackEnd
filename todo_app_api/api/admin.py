from django.contrib import admin

from .models import Group, Task, Permissions

# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'group')
    search_fields = ('title',)
    list_filter = ('stage', 'group')

@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'group')
    search_fields = ('user',)
    list_filter = ('level', 'group')