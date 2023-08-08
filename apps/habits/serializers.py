from rest_framework import serializers

from apps.habits.models import Habit
from apps.habits.validators import *


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardRelatedHabitValidator(),
            ExecutionTimeValidator(field='execution_time'),
            IsPleasantValidator(),
            FrequencyValidator(field='frequency')
        ]
