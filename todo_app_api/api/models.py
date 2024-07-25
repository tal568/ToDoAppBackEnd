from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    stage=models.CharField(max_length=100)
    group=models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks',blank=True)
    
    def save(self, *args, **kwargs):
        if not self.group: 
            raise ValueError('Group is required')
        super(Task, self).save(*args, **kwargs)

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
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='permissions',blank=True)
    def __str__(self):
        return self.user
    def save(self, *args, **kwargs):
        if not self.group:
            raise ValueError('Group is required')
        super(Permissions, self).save(*args, **kwargs)

