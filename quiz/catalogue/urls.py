from django.urls import path
from . import views
app_name = 'catalogue'


urlpatterns= [
   path('', views.index, name='index'),
   path ('dashboard/',views.dashboard, name='dashboard'),
   path ('category/<int:pk>/',views.category, name='category'),
   path('question/<int:pk>/',views.question ,name='question' ),
   path ('score/',views.score, name='score'),
    
]
    
