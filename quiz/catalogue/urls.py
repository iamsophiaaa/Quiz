from django.urls import path
from . import views
from .views import index, quiz, dashboard, score
app_name = 'catalogue'


urlpatterns= [
   path('', views.index, name='index'),
   path ('dashboard/',views.dashboard, name='dashboard'),
   path('quiz/<int:pk>/',views.quiz ,name='quiz' ),
   path ('score/',views.score, name='score'),
    
]
    
