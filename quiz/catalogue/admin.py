from django.contrib import admin
# Register your models here.
from .models import Category, Question, Option, Quiz



admin.site.register([Category, Question , Option, Quiz])