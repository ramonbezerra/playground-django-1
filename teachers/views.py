from django.shortcuts import render

from teachers.models import Teacher, TeacherForm

def teachers_list(request):
    context = {'teachers': Teacher.objects.all()}
    return render(request, 'teachers/index.html', context)

def teacher_detail(request, teacher_id):
    context = {'teacher': Teacher.objects.get(pk=teacher_id)}
    return render(request, 'teachers/detail.html', context)

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.create(**form.cleaned_data)
            teacher.save()
            return teacher_detail(request, teacher.id)
        else: 
            return render(request, 'teachers/create.html', {'form': form})
    return render(request, 'teachers/create.html', {'form': TeacherForm()})