from rest_framework import serializers

from apps.habits.models import Habit
from apps.habits.validators import RelatedHabitValidator, PleasantHabitValidator, RewardAndRelatedValidator, \
    FrequencyValidator, EtaValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for the habit model.

    Fields:
    - owner (ForeignKey): The user associated with the habit.
    - place (CharField): The place where the habit is performed.
    - time (TimeField): The time when the habit is performed.
    - action (CharField): The action of the habit.
    - is_pleasant (BooleanField): Indicates whether the habit is pleasant or not.
    - related_habit (ForeignKey): A related habit, if any. Can be NULL.
    - frequency (PositiveIntegerField): The frequency of the habit.
    - reward (CharField): The reward for completing the habit. Can be NULL.
    - eta (PositiveIntegerField): The estimated time required to complete the habit.
    - is_public (BooleanField): Indicates whether the habit is public or not.
    """
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedHabitValidator(field='related_habit'),
            PleasantHabitValidator(field='is_pleasant'),
            RewardAndRelatedValidator(),
            FrequencyValidator(field='frequency'),
            EtaValidator(field='eta')
        ]
