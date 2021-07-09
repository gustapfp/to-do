from django.db import models
# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100)
    task_deadline = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name