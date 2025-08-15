from django.shortcuts import render

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# tasks/views.py

from django.http import JsonResponse

def task_list(request):
    return JsonResponse({"message": "Task list works!"})
