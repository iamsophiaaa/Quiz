from django.shortcuts import render, redirect
from .models import Category

def index(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        
        
        return render(request, 'index.html', {'categories': categories})

