from django.urls import path, include

from students import views

appname = 'students'

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('<int:student_id>', views.student_detail, name='student_detail'),
    path('create/', views.student_create, name='student_create'),
]

students_patterns = (urlpatterns, appname)

urlpatterns = [
    path('', include(students_patterns)),
]