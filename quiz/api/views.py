import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from quiz.models import *
from .utils_random import *


class QuestionListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = QuestionSerialzer
    queryset = Question.objects.all()


class FilteredQuestionListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = QuestionSerialzer
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['difficulty', 'quiz']


class QuizTakerCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = QuizTakerEditSerializer


class QuizTakerRetrievUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = QuizTakerEditSerializer
    queryset = QuizTaker.objects.all()
    lookup_field = 'id'


class TakenQuiztAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = TakenQuizInlineSerializer
    queryset = TakenQuiz.objects.all()


class QuizListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = QuizSerialzer
    queryset = Quiz.objects.all()


# def get_queryset(self):
#     qs = Question.objects.all()
#     difficulty = self.request.GET.get('difficulty')
#     quiz = self.request.GET.get('quiz')
#     if difficulty is not None and quiz is not None:
#         qs = qs.filter(difficulty__icontains=difficulty, quiz__icontains=quiz)
#     return qs


class AnswerListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = AnswerSerialzer
    queryset = Answer.objects.all()


class QuestionsAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        difficulty = data.get('difficulty')
        quiz = data.get('quiz')

        # -------------Logic for single question--------------------

        # question = get_question(difficulty=difficulty, operation=quiz)
        # A = question.get('operator1')
        # B = question.get('operator2')
        # ans = str(question.get('answer'))
        # question_text = str(A) + str(quiz) + str(B)

        # -----------------------------------------------------------

        quiz_data_dic = {'quiz': quiz}
        difficulty_data_dic = {'difficulty': difficulty}
        data = dict()
        data.update(quiz_data_dic)
        data.update(difficulty_data_dic)
        questions = []
        for i in range(1, 31):
            question = get_question(difficulty=difficulty, operation=quiz)
            A = question.get('operator1')
            B = question.get('operator2')
            ans = question.get('answer')

            shuffled_ans = remove_duplicate(str(ans))
            question_text = str(A) + str(quiz) + str(B) + " = " + "?"
            case = {'index': str(i),
                    'question': question_text,
                    'answer': str(ans),
                    'option1': str(shuffled_ans[0]),
                    'option2': str(shuffled_ans[1]),
                    'option3': str(shuffled_ans[2]),
                    'option4': str(shuffled_ans[3]),
                    }
            questions.append(case)
            data['questions'] = questions

        return Response(data=data)

# class FilteredQuestionListAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = QuestionSerialzer

# queryset = Question.objects.all()
# filter_backends = [DjangoFilterBackend]
# filterset_fields = ['difficulty', 'quiz']

# def post(self, request, *args, **kwargs):
#     data = request.data
#     difficulty = data.get('difficulty')
#     quiz = data.get('quiz')
#     # qs = Question.objects.filter(difficulty=difficulty, quiz=quiz)
#     questions_list = []
#     quiz_obj = Quiz.objects.get(name=quiz)
#     for i in range(1, 31):
#         question = get_question(difficulty=difficulty, operation=quiz)
#         A = question.get('operator1')
#         B = question.get('operator2')
#         ans = question.get('answer')
#         question_text = str(A) + str(quiz) + str(B) + " = " + "?"
#         shuffled_ans = remove_duplicate(str(ans))
#
#         qs = Question.objects.create(
#                                      quiz=quiz_obj,
#                                      label=question_text,
#                                      difficulty=difficulty,
#                                      option1=str(shuffled_ans[0]),
#                                      option2=str(shuffled_ans[1]),
#                                      option3=str(shuffled_ans[2]),
#                                      option4=str(shuffled_ans[3]),
#                                      )
#         ans = Answer.objects.create(
#                                     question=qs,
#                                     text=str(ans),
#                                     )
#         questions_list.append(qs)
#     serializer = QuestionSerialzer(data=questions_list, many=True)
#     if serializer.is_valid():
#         return Response(serializer.validated_data)
#     return Response(serializer.errors)
