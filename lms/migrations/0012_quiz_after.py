# Generated by Django 4.1.3 on 2023-07-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0011_alter_progress_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='After',
            field=models.IntegerField(default=1, verbose_name='After Which Slide'),
        ),
    ]