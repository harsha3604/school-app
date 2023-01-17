from django import forms
from teacher.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question','answer']
