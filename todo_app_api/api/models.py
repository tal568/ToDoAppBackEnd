from django.db import models
from enum import Enum



class ActionType(str, Enum):
    owner = "owner"
    readonly = "readonly"
    readwrite = "readwrite"
    @classmethod
    def choices(cls):
        return [(key.name,key.value) for key in cls]
class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    stage = models.CharField(max_length=100)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="tasks", blank=True
    )

    def save(self, *args, **kwargs):
        if not self.group:
            raise ValueError("Group is required")
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Permissions(models.Model):
    user = models.CharField(max_length=15)
    print(ActionType.readonly)
    level = models.CharField(max_length=10, choices=ActionType.choices())
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="permissions", blank=True
    )

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.group:
            raise ValueError("Group is required")
        super(Permissions, self).save(*args, **kwargs)