from django.contrib import admin
from .models import Assignment


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_by')
    list_filter = ('title',)


admin.site.register(Assignment, AssignmentAdmin)
