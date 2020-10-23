# from django.contrib.auth.models import User
from django.db import models

DIFFICULTY_CHOICES = (
    ('B', 'Basic Level'),
    ('I', 'Intermediate Level'),
    ('A', 'Advance Level'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=1000)
    value = models.CharField(max_length=10, blank=True, null=True)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    questionid = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    label = models.CharField(max_length=1000)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Answer(models.Model):
    answerid = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizTaker(models.Model):
    user = models.CharField(max_length=60)
    age = models.IntegerField()
    correct_answers = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + " ID:" + str(self.pk)


class TakenQuiz(models.Model):
    name = models.CharField(max_length=60)
    question_count = models.IntegerField(default=30, blank=True, null=True)
    correct = models.IntegerField(default=0, blank=True, null=True)
    completed = models.BooleanField(default=False)
    quiztaker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE, related_name='takenquiz', blank=True, null=True)

    def __str__(self):
        return self.name
