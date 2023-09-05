from rest_framework.serializers import ValidationError


class PleasantAndRewardValidator:
    """Проверка на отсутствие связанности привычки и наличия вознаграждения."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get("is_pleasant") is False:
            if dict(value).get("reward") and dict(value).get("related"):
                raise ValidationError("Приятная привычка не вознаграждается")
            elif (
                dict(value).get("reward") is None
                and
                dict(value).get("related") is None
            ):
                raise ValidationError("Должна быть награда")


class DurationValidator:
    def __init__(self, field):
        self.field = field
        """Проверка длительности выполнения привычки"""

    def __call__(self, value):
        if dict(value).get(self.field):
            if dict(value).get(self.field) > 120:
                raise ValidationError(
                    "Время выполнения должно быть не больше 120 секунд"
                )

            elif dict(value).get(self.field) == 0:
                raise ValidationError("Значение должно быть больше 0")


class PleasantValidator:
    """
    В связанные привычки могут попадать только
    привычки с признаком приятной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("related") and value.get("related").is_pleasant is False:
            raise ValidationError("Связанная привычка должна быть приятной")


class PeriodValidator:
    """Период выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field):
            if dict(value).get(self.field) > 7:
                raise ValidationError("Период не должен превышать 7 дней.")
            if dict(value).get(self.field) == 0:
                raise ValidationError("Период не может быть равен 0")
            return value