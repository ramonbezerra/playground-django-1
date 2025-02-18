from django.urls import include, path

from projects import views

appname = 'projects'

patterns = [
    path('', views.projects_list, name='projects_list'),
    path('<int:project_id>', views.project_detail, name='project_detail'),
    path('create/', views.create_project, name='create_project'),
]

projects_patterns = (patterns, appname)

urlpatterns = [
    path('', include(projects_patterns)),
]