
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import APIView
from .serializers import BlogUserSerializer  
from .models import BlogUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .generate_tokens import get_tokens_for_user, get_new_access_token_for_user
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError




class SignupApiView(GenericAPIView,CreateModelMixin ):
    serializer_class = BlogUserSerializer
    queryset = BlogUser.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class SigninApiView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = authenticate(username=username, password=password)     
            if not user: 
                raise AuthenticationFailed()

            tokens = get_tokens_for_user(user)

            return Response({"success":tokens},status=status.HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class NewAccessToken(APIView):
    def post(self,request):
        # Extract the refresh token from the request data
        # refresh_token = request.data.get('refresh')

        #  if the token is passed in the headers we try this method
        try:
            refresh_token = request.headers.get('Authorization')
            if not refresh_token or not refresh_token.startswith("Bearer "):
                return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)
            refresh_token = refresh_token.split(" ")[1]
            refresh = RefreshToken(refresh_token)
            username = refresh['username']
 
            valid_username = BlogUser.objects.get(username=username)
            if not valid_username:
                raise AuthenticationFailed(detail='Invalid token')

            new_access_token = get_new_access_token_for_user(valid_username)
            return Response(new_access_token,status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


 