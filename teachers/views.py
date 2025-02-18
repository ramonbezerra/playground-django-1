from django.shortcuts import render

from teachers.models import Teacher, TeacherForm

def teachers_list(request):
    context = {'teachers': Teacher.objects.all()}
    return render(request, 'teachers/index.html', context)

def teacher_detail(request, teacher_id):
    context = {'teacher': Teacher.objects.get(pk=teacher_id)}
    return render(request, 'teachers/detail.html', context)