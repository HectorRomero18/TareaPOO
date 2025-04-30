from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=230)

    def __str__(self):
        return f"Name: {self.name}"

class Task(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField()
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE, 
                                related_name='tasks')
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Title: {self.title}  Description: {self.description}  Project: {self.project}"