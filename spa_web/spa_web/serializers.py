from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if self.instance:
            if self.instance.related_habit and (data.get('Вознаграждение') or data.get('Связанная привычка')):
                raise serializers.ValidationError('Нельзя одновременно выборать связанную привычку и вознаграждения')
            elif self.instance.is_pleasant and (data.get('Вознаграждение') or data.get('Связанная привычка')):
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
            elif data.get('is_pleasant') and (self.instance.reward or self.instance.related_habit):
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
            elif data.get('Связанная привычка'):
                if data.get('Связанная привычка').is_pleasant is False:
                    raise serializers.ValidationError('Связанная привычка должна быть приятной')
            elif data.get('Время на выполнение'):
                if data.get('Время на выполнение') > 120:
                    raise serializers.ValidationError('ExecВремя выполнения должно быть не больше 120 секунд.')
            elif data.get('Периодичность'):
                if data.get('Периодичность') > 7:
                    raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

        return data

    class Meta:
        model = Habit
        fields = '__all__'