from django.urls import path
from . import views

app_name = 'vision'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('academics/', views.academics, name='academics'),
    path('admissions/apply/', views.admissions_apply, name='admissions_apply'),
    path('admissions/success/', views.admissions_success, name='admissions_success'),
    path('student-life/', views.student_life, name='student_life'),
    path('parents/', views.parents, name='parents'),
]
