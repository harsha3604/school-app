from django.db import models
from user.models import *
# Create your models here.
class Question(models.Model):

    question = models.TextField(max_length=200,default='Question Here.')
    answer = models.TextField(max_length=200,default='Answer Here.')
    user = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.question
