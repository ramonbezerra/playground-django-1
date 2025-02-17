from django.shortcuts import render

from students.models import Student, StudentForm

def students_list(request):
    context = {'students': Student.objects.all()}
    return render(request, 'students/index.html', context)

def student_detail(request, student_id):
    context = {'student': Student.objects.get(pk=student_id)}
    return render(request, 'students/detail.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if not form.is_valid():
            return render(request, 'students/create.html', {'form': form})
        else:
            student = Student.objects.create(**form.cleaned_data)
            student.save()
            return render(request, 'students/detail.html', {'student': student})
    return render(request, 'students/create.html', {'form': StudentForm()})