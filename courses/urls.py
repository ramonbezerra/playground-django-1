from django.urls import include, path

from courses import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
]