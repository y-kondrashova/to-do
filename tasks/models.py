from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.content
