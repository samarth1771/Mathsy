# Generated by Django 2.2.3 on 2020-10-16 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20201016_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='taken_quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.TakenQuiz'),
            preserve_default=False,
        ),
    ]
