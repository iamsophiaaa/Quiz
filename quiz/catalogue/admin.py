from django.contrib import admin
# Register your models here.
from .models import Category, Question, Option



admin.site.register([Category, Question , Option])