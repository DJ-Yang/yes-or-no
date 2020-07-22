from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.
class Notice(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)