from django.shortcuts import get_object_or_404, render
from .models import Category, Question, Option

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
        for question in questions:
            options = Option.objects.filter(question=question)
        return render(request, 'quiz.html', {'category':category, 'questions': questions, 'options': options})
    


