from rest_framework import serializers

from apps.habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if self.instance:
            if self.instance.related_habit and (data.get('reward') or data.get('related_habit')):
                raise serializers.ValidationError('You cannot choose a reward and related habit for one habit')
            elif self.instance.is_pleasant and (data.get('reward') or data.get('related_habit')):
                raise serializers.ValidationError('A pleasant habit cannot have a reward or an related habit')
            elif data.get('is_pleasant') and (self.instance.reward or self.instance.related_habit):
                raise serializers.ValidationError('A pleasant habit cannot have a reward or an related habit')
            elif data.get('related_habit'):
                if data.get('related_habit').is_pleasant is False:
                    raise serializers.ValidationError('A related habit should be pleasant')
            elif data.get('execution_time'):
                if data.get('execution_time') > 120:
                    raise serializers.ValidationError('Execution time of your habit should be no more than 120 seconds')
            elif data.get('frequency'):
                if data.get('frequency') > 7:
                    raise serializers.ValidationError('You cannot perform a habit less than 1 time in 7 days.')

        return data

    class Meta:
        model = Habit
        fields = '__all__'
