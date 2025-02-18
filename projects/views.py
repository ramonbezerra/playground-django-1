from django.shortcuts import render

from projects.models import Project, ProjectForm

def projects_list(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'projects/index.html', context)

def project_detail(request, project_id):
    context = {'project': Project.objects.get(pk=project_id)}
    return render(request, 'projects/detail.html', context)

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if not form.is_valid():
            return render(request, 'projects/create.html', {'form': form})
        else:
            project = Project.objects.create(**form.cleaned_data)
            project.save()
            return render(request, 'projects/detail.html', {'project': project})
    return render(request, 'projects/create.html', {'form': ProjectForm()})