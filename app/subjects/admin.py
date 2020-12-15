from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    ordering = ("title",)


admin.site.register(Subject, SubjectAdmin)
