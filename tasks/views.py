from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskMarkDoneView(generic.View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = True
        task.save()
        return redirect('tasks:task-list')


class TaskMarkUndoneView(generic.View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = False
        task.save()
        return redirect('tasks:task-list')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
