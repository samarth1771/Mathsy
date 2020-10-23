from django.contrib import admin
from .models import *


class TakenQuizInline(admin.TabularInline):
    model = TakenQuiz


class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [TakenQuizInline]


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(TakenQuiz)
