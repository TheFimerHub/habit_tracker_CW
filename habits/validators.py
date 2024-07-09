# habits/validators.py

from django.core.exceptions import ValidationError

class HabitValidator:
    def __call__(self, habit):
        pleasant_habit = habit.get('pleasant_habit')
        related_habit = habit.get('related_habit')
        reward = habit.get('reward')
        duration = habit.get('duration')
        frequency = habit.get('frequency')

        self.validate_related_habit_and_reward(pleasant_habit, related_habit, reward)
        self.validate_duration(duration)
        self.validate_frequency(frequency)

    def validate_related_habit_and_reward(self, pleasant_habit, related_habit, reward):
        if pleasant_habit and related_habit:
            raise ValidationError('Pleasant habits cannot have a related habit.')
        if pleasant_habit and reward:
            raise ValidationError('Pleasant habits cannot have a reward.')
        if related_habit and reward:
            raise ValidationError('A habit cannot have both a related habit and a reward.')

    def validate_duration(self, duration):
        if duration >= 120:
            raise ValidationError('The duration of the habit cannot exceed 120 seconds.')

    def validate_frequency(self, frequency):
        if frequency:
            if frequency <= 1 or frequency >= 7:
                raise ValidationError('The frequency must be between 1 and 7 days.')
