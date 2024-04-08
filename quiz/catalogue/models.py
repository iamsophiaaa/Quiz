from django.db import models


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question  = models.CharField(max_length = 255)
    answer = models.CharField(max_length = 255, default="")
    

    def __str__(self):
        return self.question
    
class Option(models.Model):
    question_id= models.ForeignKey(Question, on_delete=models.CASCADE, related_name = 'options')
    option = models.CharField(max_length=255)

    def __str__(self):
        return self.option
