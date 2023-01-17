from django.db import models
from django.contrib.auth.models import User,AbstractUser

SUBJECT_CHOICES=(
    ('maths','MATHS'),
    ('science','SCIENCE'),
    ('geography','GEOGRAPHY'),
    ('english','ENGLISH'),
)
class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.TextField(max_length=100,default='None',null=True)
    age = models.IntegerField(null=True) 
    t_subject = models.CharField(max_length = 20,null=True,choices = SUBJECT_CHOICES)

    def __str__(self):
        return self.user.username 



 
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.TextField(max_length=100,default='None',null=True)
    age = models.IntegerField(null=True) 

    def __str__(self):
        return self.user.username  











