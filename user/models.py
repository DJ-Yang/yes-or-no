from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager as DefaultUserManager
import json

class UserManager(DefaultUserManager):
    def get_or_create_kakao_user(self, user_pk, extra_data):

        user = User.objects.get(pk=user_pk)        
        print('manager',user)
        user.user_type = 'K'
        user.nickname = extra_data['properties'].get('nickname','')
        user.gender = extra_data['kakao_account'].get('gender','')
        user.age_range = extra_data['kakao_account'].get('age_range','')
        user.save()

        print(user)

        return user
        

    def create_user(self, username, password=None):        
        
        user = self.model(                
            username = username        
        )        
        user.set_password(password)        
        user.save(using=self._db)        

        return user     

    def create_superuser(self, username, password ):        
       
        user = self.create_user(                   
            username = username,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

class User(AbstractBaseUser,PermissionsMixin):

    objects = UserManager()
    
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    user_type = models.CharField(max_length=10)
    nickname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    age_range = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)   
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'