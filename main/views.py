from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filter import StudentFilter
from django.core.paginator import Paginator
from .forms import StudentForm


def home(request):
    return render(request, 'main/home.html')


def register(request):
    form = StudentForm()
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            print('yes')
            form.save()
            return redirect('stsmhome')
        else:
            print(form.errors.as_data())
            form = StudentForm(request.POST)
    context = {'form': form}
    return render(request, 'main/register.html', context)


def display(request):
    students = StudentList.objects.all().filter(
        enrolment_status='ADMITTED').order_by('name')
    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs
    the_paginator = Paginator(students, 50)
    page = request.GET.get('page')
    student_in_page = the_paginator.get_page(page)
    return render(request, 'main/display.html', {'myFilter': myFilter, 'student_in_page': student_in_page})

# Create your views here.