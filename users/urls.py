from django.urls import path
from .views import SignupApiView,SigninApiView,NewAccessToken
from rest_framework_simplejwt.views import TokenBlacklistView
 

urlpatterns = [
    path('signup', SignupApiView.as_view(), name='signup'),
    path('signin',SigninApiView.as_view(),name='signin'),
    path('new-accesstoken',NewAccessToken.as_view(),name='new_access_token'),
    path('invalidate_token',TokenBlacklistView.as_view(),name='invalidate_token')
    ]
     