# Generated by Django 4.0.5 on 2022-06-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclass',
            name='attending_students',
            field=models.ManyToManyField(to='main.student'),
        ),
    ]