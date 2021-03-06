# Generated by Django 4.0.5 on 2022-06-14 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_student_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to=settings.AUTH_USER_MODEL, verbose_name='parent'),
        ),
    ]
