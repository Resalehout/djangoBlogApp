from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
#make migrations for every model you make. python manage.py makemigrations <appname>
#then you migrate again. python manage.py migrate <appname>
#create user. python manage.py createsuperuser