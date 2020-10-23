from django.urls import path, include
from .views import *

urlpatterns = [
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('answers/', AnswerListAPIView.as_view(), name='answer-list'),
    path('takenquiz/', TakenQuiztAPIView.as_view(), name='taken_quiz-list'),
    path('quiztaker/', QuizTakerCreateAPIView.as_view(), name='create-quiztaker'),
    path('quiztaker/<int:id>', QuizTakerRetrievUpdateAPIView.as_view(), name='retrieve-quiztaker'),
    path('quiz/', QuizListAPIView.as_view(), name='quiz-list'),
    path('filter_questions/', FilteredQuestionListAPIView.as_view(), name='filter-question-list'),
    path('random_questions/', QuestionsAPIView.as_view(), name='random-question-list'),
]
