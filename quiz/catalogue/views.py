from django.shortcuts import render, redirect
from .models import Question

def index(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        return render(request, 'player/index.html',{"questions":questions} )