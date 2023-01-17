from django.urls import path
from teacher.views import *

urlpatterns=[
    path('',TeacherHomeView.as_view(),name='teacher'),
    path('create/',TeacherCreateView.as_view(),name='teacher.create'),
    path('<int:pk>/',TeacherReadView.as_view(),name='teacher.detail'),    
    path('<int:pk>/update/',TeacherUpdateView.as_view(),name='teacher.update'),
    path('<int:pk>/delete/',TeacherDeleteView.as_view(),name='teacher.delete'),

]