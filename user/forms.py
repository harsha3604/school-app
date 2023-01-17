from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from user.models import *


class StudentSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)   
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user


        
class TeacherSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.IntegerField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
 
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )



