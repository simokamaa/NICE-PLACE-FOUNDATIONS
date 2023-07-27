from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('index/',  views.index, name='index'),
    path('Admission/', views.admission, name = 'Admission'),
    path('courses/', views.courses, name = 'courses'),
    path('clearance/', views.clearance, name= 'clearance'),
    path('user/' , views.user, name = 'user'),
    path('update/', views.update, name = 'update'),
    path('report/', views.report, name='report'),
    path('rtl/', views.rtl, name = 'rtl')
 ]