from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='chat id'),
        ),
    ]