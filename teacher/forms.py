from django import forms
from teacher.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['question','answer']
        # widgets={
        #     'question':forms.TextInput(attrs={'cols':300, 'rows': 50}),
        # }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        ##put placeholders
        self.fields['question'].widget.attrs.update({'placeholder':('Question')})
        self.fields['answer'].widget.attrs.update({'placeholder':('Answer')}) 

        ##to set the form size

        #for question
        self.fields['question'].widget.attrs['cols']=80
        self.fields['question'].widget.attrs['rows']=10

        #for answer
        self.fields['answer'].widget.attrs['cols']=80
        self.fields['answer'].widget.attrs['rows']=10


        ##to remove labels
        self.fields['question'].label=""
        self.fields['answer'].label=""

