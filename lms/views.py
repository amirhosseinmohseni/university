from django.shortcuts import render
from django.views import generic
from .models import *


def home(request):
    return render(request, 'lms/home.html')


class StudentsList(generic.ListView):
    template_name = 'lms/students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        return Student.objects.all().order_by('id')


