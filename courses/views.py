from django.shortcuts import render

from courses.models import Course

def courses_list(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'courses/index.html', context)

def course_detail(request, course_id):
    context = {'course': Course.objects.get(pk=course_id)}
    return render(request, 'courses/detail.html', context)