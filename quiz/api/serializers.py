from rest_framework import serializers
from quiz.models import *


class QuizSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class TakenQuizInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenQuiz
        # fields = '__all__'
        exclude = ('quiztaker',)


class QuizTakerEditSerializer(serializers.ModelSerializer):
    takenquiz = TakenQuizInlineSerializer(many=True, required=False)

    class Meta:
        model = QuizTaker
        fields = '__all__'
        read_only_fields = ['timestamp']

    def create(self, validated_data):
        takenquizzes = validated_data.pop('takenquiz')
        quiztaker = QuizTaker.objects.create(**validated_data)

        for takenquiz in takenquizzes:
            TakenQuiz.objects.create(**takenquiz, quiztaker=quiztaker)

        return quiztaker

    def update(self, instance, validated_data):
        takenquizzes_data = validated_data.pop('takenquiz')
        takenquizzes = instance.takenquiz.all()
        takenquizzes = list(takenquizzes)

        instance.user = validated_data.get('user', instance.user)
        instance.age = validated_data.get('age', instance.age)
        instance.correct_answers = validated_data.get('correct_answers', instance.correct_answers)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()

        if takenquizzes is None or len(takenquizzes) == 0:
            for takenquiz_data in takenquizzes_data:
                TakenQuiz.objects.create(**takenquiz_data, quiztaker=instance)

        elif len(takenquizzes) == len(takenquizzes_data):

            for takenquiz_data in takenquizzes_data:
                takenquiz = takenquizzes.pop(0)
                takenquiz.name = takenquiz_data.get('name', takenquiz.name)
                takenquiz.question_count = takenquiz_data.get('question_count', takenquiz.question_count)
                takenquiz.difficulty = takenquiz_data.get('difficulty', takenquiz.difficulty)
                takenquiz.correct = takenquiz_data.get('correct', takenquiz.correct)
                takenquiz.completed = takenquiz_data.get('completed', takenquiz.completed)
                takenquiz.save()

        else:

            takenquizzes_data = takenquizzes_data[len(takenquizzes):]

            for takenquiz_data in takenquizzes_data:
                TakenQuiz.objects.create(**takenquiz_data, quiztaker=instance)

        return instance


class QuizTakerCreateSerialzer(serializers.ModelSerializer):
    # taken_quiz = serializers.SerializerMethodField()
    takenquiz = TakenQuizInlineSerializer(many=True)

    class Meta:
        model = QuizTaker
        fields = '__all__'


class AnswerSerialzer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerialzer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    answer = serializers.SerializerMethodField()

    # answer = AnswerSerialzer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            "questionid",
            "quiz",
            "label",
            "answer",
            "difficulty",
            "option1",
            "option2",
            "option3",
            "option4",
        ]

    def get_answer(self, obj):
        answer = Answer.objects.filter(question=obj).first()
        print(answer)
        return str(answer)
