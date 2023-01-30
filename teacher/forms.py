from django import forms
from teacher.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question','answer']
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'placeholder':('Question')})
        self.fields['answer'].widget.attrs.update({'placeholder':('Answer')}) 

        self.fields['question'].label=""
        self.fields['answer'].label=""

