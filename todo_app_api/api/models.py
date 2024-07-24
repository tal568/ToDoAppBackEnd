from django.db import models
from django.forms import ValidationError

class Group(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    tasks = models.ManyToManyField('Task', related_name='groups', blank=True)
    permisons = models.ManyToManyField('Permison', related_name='groups')
    
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stage=models.CharField(max_length=100)
    


    def __str__(self):
        return self.title


    
class Permison(models.Model):
    #todo add the user token
    
    user = models.CharField(max_length=10)
    LEVEL_CHOICES = [
        ('owner', 'Owner'),
        ('readonly', 'Read Only'),
        ('readwrite', 'Read Write'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)



