from django.urls import path

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskMarkDoneView,
    TaskMarkUndoneView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/cteate/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path('task/<int:pk>/mark-done/', TaskMarkDoneView.as_view(), name='task-mark-done'),
    path('task/<int:pk>/mark-undone/', TaskMarkUndoneView.as_view(), name='task-mark-undone'),
]

app_name = "tasks"
