from django.shortcuts import render

from courses.models import Course

def courses_list(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'courses/index.html', context)
