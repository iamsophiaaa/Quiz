from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000)

    def __str__(self):
        return self.question
    
class Option(models.Model):
    question = models.ForeignKey(Question , on_delete =  models.CASCADE)