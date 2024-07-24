from django.db import models
from django.forms import ValidationError

class Group(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stage=models.CharField(max_length=100)
    group=models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    


    def __str__(self):
        return self.title


    
class Permissions(models.Model):
    #todo add the user token
    
    user = models.CharField(max_length=10)
    LEVEL_CHOICES = [
        ('owner', 'Owner'),
        ('readonly', 'Read Only'),
        ('readwrite', 'Read Write'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='permissions', null=True, blank=True)



