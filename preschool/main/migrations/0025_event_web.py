# Generated by Django 4.0.5 on 2022-07-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='web',
            field=models.URLField(blank=True, verbose_name='Web Address'),
        ),
    ]
