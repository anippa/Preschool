# Generated by Django 4.0.5 on 2022-06-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_schoolclass_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='attending_student',
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='attending_students',
            field=models.ManyToManyField(to='main.student'),
        ),
    ]
