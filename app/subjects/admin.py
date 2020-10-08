from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "user"]
    ordering = ["title"]

admin.site.register(Subject, SubjectAdmin)

