# Generated by Django 4.1.3 on 2023-06-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_progress_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='Status',
            field=models.CharField(max_length=30),
        ),
    ]
