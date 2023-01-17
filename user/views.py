from django.shortcuts import redirect,render
from django.contrib.auth import login,authenticate
from user.models import *
from user.forms import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

######################################################### SIGNUP,LOGIN,LOGOUT FOR STUDENT AND TEACHERS ############################
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'user/login.html', {'form': form, 'msg': msg})

class LogoutInterfaceView(LoginRequiredMixin,LogoutView):
    template_name='user/logout.html'

class IndexView(TemplateView):
    template_name='user/index.html'
######################################################### SIGNUP,LOGIN,LOGOUT FOR STUDENT AND TEACHERS ############################



