from django.db import models
from django.contrib.auth.models import User,AbstractUser

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.TextField(max_length=100,default='None')
    age = models.IntegerField(default=20) 

    def __str__(self):
        return self.user.username 

 
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.TextField(max_length=100,default='None')
    age = models.IntegerField(default=10) 

    def __str__(self):
        return self.user.username  











