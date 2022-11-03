from django.urls import URLPattern, path
from .views import TaskList , DetailList , CreateList , UpdateList , DeleteList



urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',DetailList.as_view(),name='task'),
    path('task-create',CreateList.as_view(),name='task-create'),
    path('task-update/<int:pk>/',UpdateList.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',DeleteList.as_view(),name='task-delete'),
]
