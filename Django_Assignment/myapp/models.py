from django.db import models

# Create your models here.
class Task(models.Model):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=TODO)

    def __str__(self):
        return self.title