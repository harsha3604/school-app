from django.urls import path
from student.views import *

urlpatterns=[
    path('',StudentHomeView.as_view(),name='student'),
    path('quiz/',quiz,name='student.quiz'),
    path('result/',StudentResultView.as_view(),name='student.result'),

]