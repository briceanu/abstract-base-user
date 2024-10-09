from django.urls import path
from .views import ListCreateBlog


urlpatterns = [
    path('list_create_blogs', ListCreateBlog.as_view(), name='list_create'),
    ]
     

