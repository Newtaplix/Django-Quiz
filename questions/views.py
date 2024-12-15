from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate
from .models import (QuizType, Answer, Question, UserAnswer, UserScores)
from Account.models import Account
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.
def home(request):
    ranking = UserScores.objects.all().order_by('-score')[:3]
    quiz_category = QuizType.objects.all()
    context = {
        "rank": ranking,
        "quiz": quiz_category,
    }

    return render(request, "questions/base.html", context)

def GetQuestions(request, quiz_id):
    quiz = QuizType.objects.get(id=quiz_id)
    quiz_name = quiz.title
    set = Question.objects.all().filter(category__id = quiz_id)
    answers = Answer.objects.all()
    paginator = Paginator(set, 1)
    page = request.GET.get('page')

    try:
        selector = paginator.page(page)
    except PageNotAnInteger:
        selector = paginator.page(1)
    except EmptyPage:
        selector = paginator.page(paginator.num_pages)
    user = request.user
    request.session['rel_quiz_id'] = quiz_id
    if user.is_authenticated:
        context = {
            "question": selector,
            "ans": answers,
        }

        if request.method == 'POST':
            exists = True
            user_choice = []
            correct_answers = 0
            for question in set:
                selected = request.POST.get(f'{ question }')
                perquest = Answer.objects.all().get(is_correct= True, question__text=question.text)
                if selected:
                    selected_choice = Answer.objects.filter(option=selected).get()
                    user_choice.append(selected_choice)
                    for choice in user_choice:
                        done = UserAnswer(username=user.username,
                                          quiz=quiz_name,
                                          user_choice=choice,
                                            qestion=question, 
                                            correct_answer=perquest)
                        try:
                            done = UserAnswer.objects.get(username=user.username,
                                          quiz=quiz_name,
                                            qestion=question, 
                                            correct_answer=perquest)
                            print(f'{ question }_{ question.id }')
                           
                        except ObjectDoesNotExist:
                            done.save()
                            print(f'{ question }_{ question.id }')
                            exists = False
                            print(user_choice)
                        except MultipleObjectsReturned:
                            exists = True


                    if selected_choice.is_correct:
                        correct_answers += 1
                        context["correct"] = correct_answers
            if exists:
                context['submitted'] = "Can't submit question twice"
            else:
                context['submitted'] = "Answer has been submitted."
        else:
            print("No form was submitted")
  
    return render(request, "questions/quizzes.html", context)
def QuestResults(request):
    context = {}
    quiz_id = int(request.session.get('rel_quiz_id'))
    user = request.user
    quiz_name = QuizType.objects.get(id=quiz_id)
    correct_ans = UserAnswer.objects.all().filter(correct_answer=F('user_choice'), 
                                                  username=user.username,
                                                  quiz=quiz_name.title).count()
    score = correct_ans * 5
    if request.method == "POST":
        img =  Account.objects.get(username=user.username)
        contact = request.POST.get("contact")
        info = UserScores(username=user.username, quiz=quiz_name.title, score=score,contact=contact,user_image=img.user_image,)
        try:
            info = UserScores.objects.get(username=user.username, quiz=quiz_name.title,contact=contact)
            context['score_submit'] = "User can't participate in quiz twice."
        except ObjectDoesNotExist:
            info.save()
            context['score_submit'] = "Quiz data saved successfully."
    
    context["ans"] = correct_ans
    context['user'] = user.username
    context["score"] = score
    context["quiz_title"] = quiz_name.title
    context["pip"] = quiz_id
    return render(request, "questions/done.html", context)

def Ranking(request):
    context = {}
    rank = UserScores.objects.all().order_by("-score")
    context['rank'] = rank
    return render(request, "questions/ranking.html", context)