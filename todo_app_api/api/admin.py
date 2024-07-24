from django.contrib import admin

from .models import Group, Task, Permissions

# Register your models here.

admin.site.register(Group)
admin.site.register(Task)
admin.site.register(Permissions)