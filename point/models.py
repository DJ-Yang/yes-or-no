from django.db import models
from user.models import User

class PointManager(models.Manager):
    
    def addPoint(self, pk, point):
        user_point = Point.objects.get(pk=pk)
        user_point.point += point
        user_point.save()
    
    def subPoint(self, pk, point):
        user_point = Point.objects.get(pk=pk)
        user_point.point += point
        user_point.save()


class Point(models.Model):
    point = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = PointManager()

