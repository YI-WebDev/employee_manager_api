from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birth_date', 'department', 'joined_date', 'termination_date')
    list_filter = ('gender', 'department')
    search_fields = ('name', 'department')
    ordering = ('name',)
    date_hierarchy = 'joined_date'
