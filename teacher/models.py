from django.db import models
from user.models import *
# Create your models here.
class Question(models.Model):

    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=200)
    user = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    q_subject = models.CharField(max_length=25,null=True,blank=True,choices = SUBJECT_CHOICES)

    def __str__(self):
        return self.question

    # save attribute of model A to model B: Model B should be applied at super() function. 
    # reference:https://stackoverflow.com/questions/44421024/django-model-field-with-default-value-from-another-model
    
    def save (self,*args,**kwargs):
        if self.q_subject is None:
            self.q_subject= self.user.t_subject
        return super(Question, self).save(*args,**kwargs)

