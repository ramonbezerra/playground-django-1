from django.urls import include, path

from courses import views

appname = 'courses'

patterns = [
    path('', views.courses_list, name='courses_list'),
    path('<int:course_id>', views.course_detail, name='course_detail'),
]

courses_patterns = (patterns, appname)

urlpatterns = [
    path('', include(courses_patterns)),
]