# Generated by Django 2.2.3 on 2020-10-15 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('questions_count', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=70)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('correct_answers', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionid', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=1000)),
                ('difficulty', models.CharField(choices=[('B', 'Basic Level'), ('I', 'Intermediate Level'), ('A', 'Advance Level')], max_length=1)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerid', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.Question')),
            ],
        ),
    ]
