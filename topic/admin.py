from django.contrib import admin
from .models import Topic, Selection, Notice

# Register your models here.
admin.site.register(Topic)
admin.site.register(Selection)
admin.site.register(Notice)