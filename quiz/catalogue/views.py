from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Question, Option
from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        context={}
        
        
        return render(request, 'index.html')



    
def dashboard(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        
        
        return render(request, 'dashboard.html', {'categories': categories})


def quiz(request, pk):
    if request.method == 'GET':
        category = get_object_or_404(Category, pk=pk)
        questions = Question.objects.filter(category=pk)
        question_options = {}
        for question in questions:
            options = Option.objects.filter(question=question)
            question_options[question] = options  # Store options for this question

        return render(request, 'quiz.html', {'category': category, 'questions':questions, 'question_options': question_options})
    
    if request.method == 'POST':
        
        return redirect('catalogue:score')
    

def score(request):
    return render(request, 'score.html')