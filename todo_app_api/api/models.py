from django.db import models
import uuid
class Group(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    id = models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stage=models.CharField(max_length=100)
    group=models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')
    


    def __str__(self):
        return self.title


    
class Permissions(models.Model):
    
    user = models.CharField(max_length=10)
    LEVEL_CHOICES = [
        ('owner', 'Owner'),
        ('readonly', 'ReadOnly'),
        ('readwrite', 'ReadWrite'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='permissions')



