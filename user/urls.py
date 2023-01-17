from django.urls import path
from user.views import *

urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('student_signup/',StudentSignUpView.as_view(),name='student_signup'),
    path('teacher_signup/',TeacherSignUpView.as_view(),name='teacher_signup'),
    path('login/',login_view,name='login'),
    path('logout/',LogoutInterfaceView.as_view(),name='logout'),
]