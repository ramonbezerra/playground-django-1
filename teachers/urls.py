from django.urls import include, path

from teachers import views

appname = 'teachers'

patterns = [
    path('', views.teachers_list, name='teachers_list'),
    path('<int:teacher_id>', views.teacher_detail, name='teacher_detail'),
    path('create/', views.teacher_create, name='teacher_create'),
]

teachers_patterns = (patterns, appname)

urlpatterns = [
    path('', include(teachers_patterns)),
]