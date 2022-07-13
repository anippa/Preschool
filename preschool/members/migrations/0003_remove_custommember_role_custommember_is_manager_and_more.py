# Generated by Django 4.0.5 on 2022-06-27 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_custommember_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custommember',
            name='role',
        ),
        migrations.AddField(
            model_name='custommember',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custommember',
            name='is_parent',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='custommember',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]