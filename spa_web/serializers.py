from rest_framework import serializers
from .models import Habit, Place
from .validators import (
    PleasantAndRewardValidator,
    DurationValidator,
    PleasantValidator,
    PeriodValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    """
    Serializer for Habit model
    """

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        habit = Habit.objects.create(**validated_data)
        return habit

    class Meta:
        validators = [
            PleasantAndRewardValidator(field="is_pleasant"),
            DurationValidator(field="duration"),
            PleasantValidator(field="is_pleasant"),
            PeriodValidator(field="period"),
        ]
        model = Habit
        fields = "__all__"


class PlacesSerializer(serializers.ModelSerializer):
    """
    Serializer for Places model
    """

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        place = Place.objects.create(**validated_data)
        return place

    class Meta:
        model = Place
        fields = "__all__"