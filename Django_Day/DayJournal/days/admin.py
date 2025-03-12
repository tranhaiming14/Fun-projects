from django.contrib import admin
from .models import Day

class DayAdmin(admin.ModelAdmin):
    list_display = ('alias', 'date_time', 'workout', 'academic', 'sr', 'economics')
    search_fields = ('alias',)

admin.site.register(Day, DayAdmin)