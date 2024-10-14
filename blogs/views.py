from rest_framework.mixins import CreateModelMixin, ListModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet 
from .serializers import BlogModelSerializer
from .models import BlogModel
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status
from .permissions import AgePermission ,IsAuthenticatedAndOwner
from rest_framework.exceptions import NotFound




class ListCreateBlog(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin):
    # permission_classes =[IsAuthenticated]

    def get(self,request):
        queryset = BlogModel.objects.all()
        serializer= BlogModelSerializer(queryset,many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = BlogModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        pk = self.request.query_params.get('id')
        try:
            return BlogModel.objects.get(id=pk)
        except BlogModel.DoesNotExist:
            raise NotFound(detail=f'Car with the id {pk} not found')


    def put(self,request):
        blog =self.get_object()
        if request.user.username != blog.username.username:
# the secone username comes from the   to_field='username'
            return Response({"detail": "You do not have permission to update this blog."},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = BlogModelSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


    def get_permissions(self):
        """
        Assign different permissions based on the HTTP method.
            """
        if self.request.method == 'GET':
            # Permissions for GET requests
            permission_classes = [IsAuthenticated]
            # permission_classes = [IsAuthenticated, AgePermission]

        elif self.request.method == 'POST':
            # Permissions for POST requests
            permission_classes = [IsAuthenticated]
        elif self.request.method == 'PUT':
            # Permissions for POST requests
            permission_classes = [IsAuthenticated]
        else:
            # Default permissions for other methods, if any
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


#  remove a blog 




class RemoveBlog(GenericAPIView):
    permission_classes =[IsAuthenticatedAndOwner]

    def delete(self, request):
        pk = self.request.query_params.get('id')
        if not pk:
            return Response({'error': 'ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            blog = BlogModel.objects.get(id=pk)
        except BlogModel.DoesNotExist:
            raise NotFound(detail=f'No blog with id {pk} found')
        
        self.check_object_permissions(request, blog)
        blog.delete()
        return Response({'success': 'Blog deleted'}, status=status.HTTP_204_NO_CONTENT)
