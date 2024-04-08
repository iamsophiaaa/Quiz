from django.shortcuts import render, redirect
from .models import Question, Option

def index(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        if questions.exists():
            
            question = questions[0]
            options = Option.objects.filter(question_id=question)
        
            return render(request, 'player/index.html', {'question': question, 'options': options})

