from rest_framework.permissions import BasePermission


class AgePermission(BasePermission):

    """
    has_permission is used for making permissions to the user
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.age < 19:
            return True
        
        return False





class IsAuthenticatedAndOwner(BasePermission):
    """
    has_object_permission is used for making permissions to the object

    has_permission is a check made before calling the has_object_permission. 
    That means that you need to be allowed by has_permission before you get any chance to check the ownership 

    """
    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user.is_authenticated
        # this line returns a boolean 
        # print(request.user.is_authenticated)
        # if the user is valid return True else returns False

    def has_object_permission(self, request, view, obj):

        """
        you have to use this in the view
          try:
            blog = BlogModel.objects.get(id=pk)
        except BlogModel.DoesNotExist:
            raise NotFound(detail=f'No blog with id {pk} found')
        
        self.check_object_permissions(request, blog)
        """
        # Check if the request user is the owner of the blog (obj)
        # username = models.ForeignKey(BlogUser, 
        # to_field='username', on_delete=models.CASCADE, related_name='blogs')
        # a user can't delete a blog if it's not the owner of the blog
        return request.user == obj.username
        # returns a bolean
 

