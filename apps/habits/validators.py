from rest_framework import serializers


class RewardValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue and value.get('related_habit'):
            raise serializers.ValidationError(
                'You cannot choose a reward for this habit, because you have a related habit')


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue and value.get('reward'):
            raise serializers.ValidationError(
                'You cannot choose a related habit for this habit, because you have a reward')
        elif tmpvalue:
            if not tmpvalue.is_pleasant:
                raise serializers.ValidationError('Related habits can only include pleasant habits')


class ExecutionTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue > 120:
            raise serializers.ValidationError('Execution time of your habit should be no more than 120 seconds')


class IsPleasantValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue and value.get('reward') or value.get('related_habit'):
            raise serializers.ValidationError('A pleasant habit cannot have a reward or an related habit')

class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmpvalue = value.get(self.field)
        if tmpvalue > 7:
            raise serializers.ValidationError('You cannot perform a habit less than 1 time in 7 days.')
