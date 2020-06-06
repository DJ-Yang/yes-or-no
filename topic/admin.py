from django.contrib import admin
from .models import Topic, Selection, DailyData

# class DailyDataAdmin(admin.ModelAdmin):
#   readonly_fields = ('created_at',)

admin.site.register(Topic)
admin.site.register(Selection)
admin.site.register(DailyData)