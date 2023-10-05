# Generated by Django 4.1.3 on 2023-06-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.categories'),
        ),
        migrations.AlterField(
            model_name='course_enrollment',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='slides',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='video',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.AlterField(
            model_name='website',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.country'),
        ),
    ]
