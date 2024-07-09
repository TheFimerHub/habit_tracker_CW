from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()

class Habit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    pleasant_habit = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_to')
    frequency = models.IntegerField(default=1)  # in days
    reward = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField()  # in seconds
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.action
