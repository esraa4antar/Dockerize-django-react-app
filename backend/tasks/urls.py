from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('tasks/', views.task_list),
]
