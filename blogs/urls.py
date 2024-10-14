from django.urls import path
from .views import ListCreateBlog,RemoveBlog



urlpatterns = [
    path('list_create_blogs/', ListCreateBlog.as_view(), name='list_create'),  
    path('remove_blog',RemoveBlog.as_view(),name='remove_blog'),
]
