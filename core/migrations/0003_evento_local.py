# Generated by Django 3.2.7 on 2021-09-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210908_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.TextField(blank=True, null=True),
        ),
    ]
