# Generated by Django 4.1.3 on 2023-06-26 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_rename_categories_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.country', verbose_name='Country'),
        ),
    ]