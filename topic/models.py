from django.db import models
from django.utils import timezone
from user.models import User

# Integer 필드 최댓값 최솟값 설정을 위한 임포트
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Topic(models.Model):
  title = models.CharField(max_length=100)
  thumb_image = models.ImageField()
  description = models.TextField()
  # 임시로 CharField적용 나중에 Forignkey 로 변경
  author = models.CharField(max_length= 100, default="admin")
  selection1_image = models.ImageField()
  selection1_des = models.CharField(max_length=20)
  selection2_image = models.ImageField()
  selection2_des = models.CharField(max_length=20)
  hot_topic = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=timezone.now())

  
  def get_count_yes(self):
    total = self.selection_set.count()
    yes = self.selection_set.filter(select=0).count()

    if total != 0:
      percent = int(yes/total*100)
    else:
      percent = 0
    return f'{percent}%'

  def get_count_no(self):
    total = self.selection_set.count()
    no = self.selection_set.filter(select=1).count()
    

    if total != 0:
      percent = int(no/total*100)
    else:
      percent = 0
    return f'{percent}%'


class Selection(models.Model):
  class Sex(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
  class Select(models.IntegerChoices):
    YES = 0
    NO = 1
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  select = models.IntegerField(choices=Select.choices, null=True, blank=True)
  selector = models.ForeignKey(User, on_delete=models.CASCADE)
  age_range = models.IntegerField(validators=[
    MinValueValidator(0), 
    MaxValueValidator(100),
    ])
  gender = models.IntegerField(choices=Sex.choices)
  created_at = models.DateTimeField(auto_now=timezone.now())
  updated_at = models.DateTimeField(default=timezone.now)

