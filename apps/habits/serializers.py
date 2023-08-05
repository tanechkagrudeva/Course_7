from rest_framework import serializers

from apps.habits.models import Habit
from apps.habits.validators import *


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardValidator(field='reward'),
            RelatedHabitValidator(field='related_habit'),
            ExecutionTimeValidator(field='execution_time'),
            IsPleasantValidator(field='is_pleasant'),
            FrequencyValidator(field='frequency')
        ]
