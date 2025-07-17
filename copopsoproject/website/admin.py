from django.contrib import admin
from .models import CourseOutcome

@admin.register(CourseOutcome)
class CourseOutcomeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

# Register your models here.
