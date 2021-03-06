# Generated by Django 4.0.5 on 2022-06-13 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Last Name')),
                ('age', models.CharField(max_length=2, verbose_name='Age')),
                ('blood_type', models.CharField(max_length=2, verbose_name='Blood Type')),
                ('allergy', models.TextField(max_length=200, verbose_name='Allergies')),
                ('chronic_illness', models.TextField(max_length=200, verbose_name='Chronic Illnesses')),
                ('student_pic', models.ImageField(default='images/default_pic.jpg', upload_to='images/', verbose_name='Student Picture')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='parent')),
            ],
        ),
    ]
