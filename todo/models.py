from django.db import models
from django.utils import timezone


class TodoModel(models.Model):
    subject = models.CharField(max_length=256)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status_choices = (
        ('1', 'undone'),
        ('2', 'doing'),
        ('3', 'done'),
    )
    status = models.CharField(choices=status_choices, max_length=10, default='1', null=True)

    def __str__(self):
        return self.subject
