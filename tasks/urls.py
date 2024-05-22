from django.urls import path

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tasks/cteate/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "tasks"
