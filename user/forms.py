from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from user.models import *


class StudentSignUpForm(UserCreationForm):
    name=forms.CharField(required=True,label="")
    age=forms.IntegerField(required=True,label="")

    class Meta(UserCreationForm.Meta):
        model = User

    #remove help text from signup form 
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].widget.attrs.update({'placeholder':('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password')})
        self.fields['name'].widget.attrs.update({'placeholder':('Name')})     
        self.fields['age'].widget.attrs.update({'placeholder':('Age')})

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(
            user=user,
            name=self.cleaned_data.get('name'),
            age=self.cleaned_data.get('age'),
            )
        student.save()
        return user


        
class TeacherSignUpForm(UserCreationForm):
    name=forms.CharField(required=True,label="")
    age=forms.IntegerField(required=True,label="")
    t_subject = forms.CharField(required=True,label = "", widget = forms.Select(choices=SUBJECT_CHOICES))

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(TeacherSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].widget.attrs.update({'placeholder':('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password')})
        self.fields['name'].widget.attrs.update({'placeholder':('Name')})     
        self.fields['age'].widget.attrs.update({'placeholder':('Age')})   

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(
            user=user,
            name=self.cleaned_data.get('name'),
            age=self.cleaned_data.get('age'),
            t_subject=self.cleaned_data.get('t_subject'),
            )
        teacher.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Username",
            }
        ),
        label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Password",
            }
        ),
        label=""
    )



