from django.db import models


class Task(models.Model):
    name = models.TextField(max_length=80)
    estimated_time = models.IntegerField()
    actual_time = models.IntegerField()
    is_recurring = models.BooleanField()

    def __str__(self):
        return self.name
