from django.db import models
from Account.models import Account


# Create your models here.
class QuizType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    category = models.ForeignKey(QuizType, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.text)

class Answer(models.Model):
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    option = models.TextField(max_length=255)

    def __str__(self):
        return str(self.option)

class UserAnswer(models.Model):
    username = models.CharField(max_length=100)
    quiz = models.CharField(max_length=40,blank=True, null=True)
    user_choice = models.ForeignKey(Answer, on_delete=models.PROTECT, related_name="user_choice")
    qestion = models.ForeignKey(Question, on_delete=models.PROTECT)
    correct_answer = models.ForeignKey(Answer, on_delete=models.PROTECT)


    def __str__(self):
        return str(self.correct_answer)


class UserScores(models.Model):
    username = models.CharField(max_length=100)
    quiz = models.CharField(max_length=40,blank=True, null=True)
    score = models.CharField(max_length=3, blank=True, null=True)
    user_image = models.CharField(max_length=220,null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return str(self.username)