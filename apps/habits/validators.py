from rest_framework.serializers import ValidationError


class EtaValidator:
    """
    Validator for checking the execution time of a habit.
    Ensures that the habit execution time is within the range of 1 to 120 seconds.

    Args:
        field (str): The name of the time field in the data.

    Raises:
        ValidationError: If the execution time is outside the valid range.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 1 > value.get(self.field) or value.get(self.field) > 120:
            raise ValidationError("Время выполнения привычки не может превышать 120 секунд или быть меньше 0.")


class FrequencyValidator:
    """
    Validator for checking the frequency of habit execution.
    Ensures that the habit is not executed less frequently than once every 7 days.

    Args:
        field (str): The name of the frequency field in the data.

    Raises:
        ValidationError: If the habit frequency is less than once every 7 days.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 1 > value.get(self.field) or value.get(self.field) > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


class RelatedHabitValidator:
    """
    Validator for checking related habits.
    Ensures that related habits are marked as pleasant.

    Args:
        field (str): The name of the related habit field in the data.

    Raises:
        ValidationError: If a related habit is not marked as pleasant.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val and tmp_val.is_pleasant is False:
            raise ValidationError("Связанные привычки могут быть только приятными.")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # У приятной привычки не может быть вознаграждения или связанной привычки.
        tmp_val = dict(value)
        if tmp_val.get(self.field):
            if tmp_val.get('reward') is not None or tmp_val.get('related_habit') is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class RewardAndRelatedValidator:
    """
    Validator for checking pleasant habits.
    Ensures that pleasant habits do not have rewards or related habits at the same time.

    Raises:
        ValidationError: If a pleasant habit has a reward or related habit.
    """
    def __call__(self, value):
        tmp_val = dict(value)
        if tmp_val.get('reward') is not None and tmp_val.get('related_habit') is not None:
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и вознаграждение.')