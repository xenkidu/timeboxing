from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=80)
    estimated_time = models.IntegerField()
    actual_time = models.IntegerField(null=True, blank=True)
    is_recurring = models.BooleanField(default=True)

    def __str__(self):
        return self.name
