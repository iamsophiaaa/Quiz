from django.db import models


class Category(models.Model):
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
    
