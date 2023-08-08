from rest_framework import serializers


class RewardRelatedHabitValidator:
    def __call__(self, value):
        if value.get('reward') and value.get("related_habit"):
            raise serializers.ValidationError(
                'You cannot choose a reward and related habit for one habit')


class ExecutionTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue:
            if tmpvalue > 120:
                raise serializers.ValidationError('Execution time of your habit should be no more than 120 seconds')


class IsPleasantValidator:
    def __call__(self, value):
        if value.get('is_pleasant') is True and (value.get('reward') or value.get('related_habits')):
            raise serializers.ValidationError('A pleasant habit cannot have a reward or an related habit')


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue:
            if tmpvalue > 7:
                raise serializers.ValidationError('You cannot perform a habit less than 1 time in 7 days.')
