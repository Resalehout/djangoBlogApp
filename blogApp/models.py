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
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()
    
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
   
#make migrations for every model you make. python manage.py makemigrations <appname>
#then you migrate again. python manage.py migrate <appname>
#create user. python manage.py createsuperuser