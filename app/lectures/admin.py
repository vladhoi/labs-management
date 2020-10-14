from django.contrib import admin

from .models import Lecture


# Register your models here.

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'user')
    list_filter = ('user', 'subject')


admin.site.register(Lecture, LectureAdmin)
