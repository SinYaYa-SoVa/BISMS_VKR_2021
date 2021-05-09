from django.shortcuts import render
from django.views.generic.list import ListView
from incidents.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department
# Create your views here.

from .models import Incident

def index(request):
    response = render(request, 'index.html')
    return response

def management(request):
    response = render(request, 'management.html')
    return response


def analysis(request):
    response = render(request, 'analysis.html')
    return response

def incidents(request):
    response = render(request, 'incidents.html')
    return response

def about(request):
    response = render(request, 'about.html')
    return response



# class EmployeeView(ListView):
#     model = Employee
#     template_name = 'incidents.html'
#     context_object_name = 'employees'

# def EmpList(request):
#     data = Employee.objects.all()
#     return render(request, "incidents.html", {"employees": data})

# class EmpView(ListView):
#     template_name = 'incidents.html'
#     context_object_name = 'emp'
#     queryset = Employee.objects.all()

# class IncidentsView(APIView):
#     def get(self, request):
#         incidents = Incident.objects.all()
#         return Response({"incidents": incidents})

def itemget(request):
    data = Department.objects.all()
    context={
      'data': data
    }
    return render(request, "incidents.html", context)