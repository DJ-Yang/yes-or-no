from django.db import models
from django.contrib.utils import timezone

# Integer 필드 최댓값 최솟값 설정을 위한 임포트
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Topic(models.Model):
  title = models.CharField(max_length=100)
  thumb_image = models.ImageField()
  description = models.TextField()
  # 임시로 CharField적용 나중에 Forignkey 로 변경
  author = models.CharField(max_length= 100, default="admin")
  selection1_image = modes.ImageField()
  selection1_des = models.CharField(max_length=20)
  selection2_image = modes.ImageField()
  selection2_des = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=timezone.now())

class Selection(models.Model):
  class Sex(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  # 선택 타입 넣기 yes or no
  selector = models.CharField(max_length=20, default="selecor")
  age = models.IntegerField(validators=[
    MinValueValidator(0), 
    MaxValueValidator(100),
    ])
  sex = models.IntegerField(choices=Sex.choices)
  created_at = models.DateTimeField(auto_now=timezone.now())