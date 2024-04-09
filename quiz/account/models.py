from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    email = models.CharField(max_length = 100, verbose_name='Email')
    profile_img = models.ImageField(upload_to='profile_image', default='user.png', blank=True, null=True, verbose_name='Profile Picture')
    gender_choice = (
        ('Male', 'Male'), 
        ('Female', 'Female'), 
        ('Others', 'Others'),
    )
    gender = models.CharField(max_length=6, choices=gender_choice, blank=True, null=True)

    def __str__(self):
        return self.user.username