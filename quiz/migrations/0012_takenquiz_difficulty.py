# Generated by Django 2.2.3 on 2020-10-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20201023_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='takenquiz',
            name='difficulty',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
