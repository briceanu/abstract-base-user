from django.db import models
from users.models import BlogUser

# Create your models here.
class BlogModel(models.Model):
    username = models.ForeignKey(BlogUser, to_field='username', on_delete=models.CASCADE, related_name='blogs')
    date_published = models.DateTimeField(auto_now_add=True) 
    details = models.TextField()
    age = models.IntegerField()