from django.db import models
from django.utils import timezone
from user.models import User

# Integer 필드 최댓값 최솟값 설정을 위한 임포트
from django.core.validators import MinValueValidator, MaxValueValidator

class Topic(models.Model):
  thumb_image = models.ImageField()
  title = models.CharField(max_length=45)
  author = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)
  content = models.TextField()
  # 후에 게시판을 나누게 될 경우 고려
  # category = models.IntegerField()
  selection_amount = models.IntegerField(default=0)
  hot_topic = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=timezone.now())

class Selection(models.Model):
  topic = models.ForeignKey(Topic, related_name="selections", on_delete=models.CASCADE)
  image = models.ImageField(null=True, blank=True)
  description = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=timezone.now())

  def save(self, *args, **kwargs):
    topic = self.topic
    topic.selection_amount += 1
    topic.save()
    super().save(*args, **kwargs)

    # delete 시 삭제 항목

class Pick(models.Model):
  class Sex(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
  topic = models.ForeignKey(Topic, related_name="picks", on_delete=models.CASCADE)
  author = models.ForeignKey(User, related_name="picks", on_delete=models.CASCADE)
  selection = models.IntegerField(validators=[
    MinValueValidator(1), 
    MaxValueValidator(4),
  ], null=True)
  age_range = models.IntegerField(validators=[
    MinValueValidator(0), 
    MaxValueValidator(100),
  ])
  gender = models.IntegerField(choices=Sex.choices)
  created_at = models.DateTimeField(auto_now=timezone.now())
  updated_at = models.DateTimeField(default=timezone.now)
  
class DailyPick(models.Model):
  pick1 = models.IntegerField()
  pick2 = models.IntegerField()
  pick3 = models.IntegerField()
  pick4 = models.IntegerField()
  created_at = models.DateTimeField(auto_now=timezone.now())