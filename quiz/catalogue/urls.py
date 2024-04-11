from django.urls import path
from . import views
from .views import index, quiz, dashboard
app_name = 'catalogue'


urlpatterns= [
   path('', index, name='index'),
   path ('dashboard/',dashboard, name='dashboard'),
   path('quiz/<int:pk>/',quiz ,name='quiz' ),
    
]
    
