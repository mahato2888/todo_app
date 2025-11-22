from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('done', 'Done')], default='pending')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
