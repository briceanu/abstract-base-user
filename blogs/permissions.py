from rest_framework.permissions import BasePermission


class AgePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.age < 19:
            return True
        
        return False

    # def has_object_permission(self, request, view, obj):
    #     """ 
    #     extracting the age field from the object
    #     """
    #     age = obj.age
    #     if age > 20:
    #         return True
    #     return False    

# class CustomPermission(BasePermission):
    """
    has_permission is used for making permissions to the user
    """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated



# class CustomObjectPermission(BasePermission):
    """
    has_object_permission is used for making permissions to the object
    """
    # def has_object_permission(self, request, view, obj):
        # return request.user == obj.owner  # Allow access only if the user is the owner of the object 

    # in the blog you have to define a owner field

    # class BlogPost(models.Model):
    # title = models.CharField(max_length=255)
    # content = models.TextField()
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 