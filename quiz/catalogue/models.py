from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_name = models.CharField(max_length = 100)
    quiz_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.quiz_name

class Category(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category
    
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text[:20]
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length = 255)
    is_correct = models.BooleanField(default=True)

    def __str__(self):
        return self.option_text
    
class Score(models.Model):
    quiz = models.ForeignKey(Quiz, related_name = 'score_quiz' , on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = 'score_by' , on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name = 'score_question' , on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    answer = models.ForeignKey(Option, related_name='score_option', on_delete=models.CASCADE)