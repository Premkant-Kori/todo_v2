from django.db import models

# Create your models here.
class TaskTable(models.Model):
    task_column = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_column