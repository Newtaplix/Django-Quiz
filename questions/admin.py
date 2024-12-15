from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Question, QuizType, Answer, UserAnswer, UserScores)
# Register your models here.
# Register your models here.
@admin.register(QuizType)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title','description','date_created',]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "text",
    ]

@admin.register(Answer)
class AnswersAdmin(admin.ModelAdmin):
    list_display = [
        "question",
        "option",
        "is_correct",
    ]

@admin.register(UserAnswer)
class AnswersAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "quiz",
        "qestion",
        "user_choice",
        "correct_answer",
    ]


@admin.register(UserScores)
class AnswersAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "quiz",
        "score",
        "contact",
    ]
    ordering = ['-score']

