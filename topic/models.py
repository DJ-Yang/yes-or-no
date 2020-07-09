from django.db import models
from django.utils import timezone
from user.models import User

# Integer 필드 최댓값 최솟값 설정을 위한 임포트
from django.core.validators import MinValueValidator, MaxValueValidator

class Topic(models.Model):
  thumb_image = models.ImageField()
  title = models.CharField(max_length=45)
  # 임시로 CharField적용 나중에 Forignkey 로 변경
  author = models.CharField(max_length= 100, default="admin")
  content = models.TextField()
  # 후에 게시판을 나누게 될 경우 고려
  # category = models.IntegerField()
  selection_amount = models.IntegerField(validators=[
    MinValueValidator(2), 
    MaxValueValidator(4),
    ])
  hot_topic = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=timezone.now())

  # def get_count_yes(self):
  #   total = self.selection_set.count()
  #   yes = self.selection_set.filter(select=0).count()

  #   if total != 0:
  #     percent = int(yes/total*100)
  #   else:
  #     percent = 0
  #   return f'{percent}%'

  # def get_count_no(self):
  #   total = self.selection_set.count()
  #   no = self.selection_set.filter(select=1).count()
    

  #   if total != 0:
  #     percent = int(no/total*100)
  #   else:
  #     percent = 0
  #   return f'{percent}%'

class Selection(models.Model):
  topic = models.ForeignKey(Topic, related_name="selections", on_delete=models.CASCADE)
  image = models.ImageField()
  description = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=timezone.now())

class Pick(models.Model):
  class Sex(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
  # 임시로 CharField적용 나중에 Forignkey 로 변경
  picker = models.CharField(max_length= 100, default="admin")
  selection = models.IntegerField(validators=[
    MinValueValidator(1), 
    MaxValueValidator(4),
  ])
  age_range = models.IntegerField(validators=[
    MinValueValidator(0), 
    MaxValueValidator(100),
  ])
  gender = models.IntegerField(choices=Sex.choices)
  created_at = models.DateTimeField(auto_now=timezone.now())
  updated_at = models.DateTimeField(default=timezone.now)
  

class DailyData(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
  positive_count = models.IntegerField(null=True)
  negative_count = models.IntegerField(null=True)
  positive_male_count = models.IntegerField(null=True)
  positive_female_count = models.IntegerField(null=True)
  negative_male_count = models.IntegerField(null=True)
  negative_female_count = models.IntegerField(null=True)
  positive_10age_count = models.IntegerField(null=True)
  positive_10age_male_count = models.IntegerField(null=True)
  positive_10age_female_count = models.IntegerField(null=True)
  positive_20age_count = models.IntegerField(null=True)
  positive_20age_male_count = models.IntegerField(null=True)
  positive_20age_female_count = models.IntegerField(null=True)
  positive_30age_count = models.IntegerField(null=True)
  positive_30age_male_count = models.IntegerField(null=True)
  positive_30age_female_count = models.IntegerField(null=True)
  positive_40age_count = models.IntegerField(null=True)
  positive_40age_male_count = models.IntegerField(null=True)
  positive_40age_female_count = models.IntegerField(null=True)
  positive_50age_count = models.IntegerField(null=True)
  positive_50age_male_count = models.IntegerField(null=True)
  positive_50age_female_count = models.IntegerField(null=True)
  positive_60age_count = models.IntegerField(null=True)
  positive_60age_male_count = models.IntegerField(null=True)
  positive_60age_female_count = models.IntegerField(null=True)
  negative_10age_count = models.IntegerField(null=True)
  negative_10age_male_count = models.IntegerField(null=True)
  negative_10age_female_count = models.IntegerField(null=True)
  negative_20age_count = models.IntegerField(null=True)
  negative_20age_male_count = models.IntegerField(null=True)
  negative_20age_female_count = models.IntegerField(null=True)
  negative_30age_count = models.IntegerField(null=True)
  negative_30age_male_count = models.IntegerField(null=True)
  negative_30age_female_count = models.IntegerField(null=True)
  negative_40age_count = models.IntegerField(null=True)
  negative_40age_male_count = models.IntegerField(null=True)
  negative_40age_female_count = models.IntegerField(null=True)
  negative_50age_count = models.IntegerField(null=True)
  negative_50age_male_count = models.IntegerField(null=True)
  negative_50age_female_count = models.IntegerField(null=True)
  negative_60age_count = models.IntegerField(null=True)
  negative_60age_male_count = models.IntegerField(null=True)
  negative_60age_female_count = models.IntegerField(null=True)
  created_at = models.DateTimeField(default=timezone.now)