# Generated by Django 4.1.3 on 2023-06-27 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_alter_user_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='Country',
        ),
    ]
