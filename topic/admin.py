from django.contrib import admin
from .models import Topic, Selection, Pick, DailyPick

class SelectionInline(admin.TabularInline):
  model = Selection
  extra = 0

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

  inlines = [
    SelectionInline,
  ]

  def _selecitons(self, obj):
    return obj.selecitons.all().count()

admin.site.register(Pick)
admin.site.register(DailyPick)