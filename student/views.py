from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from teacher.models import *
from student.forms import *
from django.contrib.auth.decorators import login_required

######################################################## STUDENT VIEWS ###################################################

class StudentHomeView(LoginRequiredMixin,TemplateView):
    template_name='student/student.html'
    login_url='/login'

@login_required(login_url='/login')
def quiz(request):
    questions = Question.objects.all()
    form=AnswerForm()
    total=0
    wrong=0
    right=0
    score=0
    if request.method == "GET":
        questions = Question.objects.filter(q_subject = request.GET.get('subject-names'))

    if request.method=="POST":
        for i in Question.objects.filter(q_subject = request.GET.get('subject-names')):
                instance=i
                form = AnswerForm(request.POST)
                # print(instance)
                # print(request.POST.getlist('answer'))
                if form.is_valid():
                    if request.POST.getlist('answer')[total].strip() == instance.answer:
                        right+=1
                        score+=10
                        # print('r '+str(right))
                    else:
                        wrong+=1
                        # print('w '+str(wrong))
                    total+=1


        context={
                    'total':total,
                    'right':right,
                    'wrong':wrong,
                    'score':score,
                }
        return render(request,"student/s_result.html",context)

    context_dict = {'form':form,'questions':questions}
    return render(request,"student/s_quiz.html",context_dict)




class StudentResultView(LoginRequiredMixin,TemplateView):
    template_name = 'student/s_result.html'
    
######################################################## STUDENT VIEWS ###################################################


