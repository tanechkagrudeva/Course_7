from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="is_related",
            new_name="related",
        ),
    ]