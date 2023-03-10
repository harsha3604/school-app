from django.shortcuts import HttpResponseRedirect
from teacher.models import *
from teacher.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView

############################################################## TEACHER VIEW ##########################################################
class TeacherHomeView(LoginRequiredMixin,ListView):
    model = Question
    context_object_name="questions"
    template_name='teacher/teacher.html'
    login_url='/login'


    # this below code is for "per user"

    # def get_queryset(self):
    #     try:
    #         u=Teacher.objects.get(user=self.request.user)
    #     except Teacher.DoesNotExist:
    #         u=None
    #     return Question.objects.filter(user_id=u)


    #this code is for "per subject"
    # refernce: https://stackoverflow.com/questions/64039737/object-is-not-subscriptable-using-django-and-python
    def get_queryset(self):
        try:
            u=Teacher.objects.get(user=self.request.user)
            subject=u.t_subject
        except Teacher.DoesNotExist:
            u=None
            subject=u.t_subject
        return Question.objects.filter(q_subject=subject)



class TeacherCreateView(LoginRequiredMixin,CreateView):
    model=Question
    form_class=QuestionForm
    template_name='teacher/create.html'
    success_url = reverse_lazy('teacher')

    def form_valid(self,form):
        instance = form.save(commit=False)
        try:
            instance.user=Teacher.objects.get(user=self.request.user)
        except Teacher.DoesNotExist:
            instance.user=None
        instance.save()
        return HttpResponseRedirect('/teacher')

    
    

class TeacherReadView(LoginRequiredMixin,DetailView):
    model = Question
    context_object_name = 'questions'
    template_name='teacher/detail.html'   


class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'teacher/update.html'
    success_url = reverse_lazy('teacher')

class TeacherDeleteView(LoginRequiredMixin,DeleteView):
    model = Question
    template_name='teacher/delete.html'
    success_url = reverse_lazy('teacher')
############################################################## TEACHER VIEW ##########################################################