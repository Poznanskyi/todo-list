from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_at")

    def __str__(self) -> str:
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
