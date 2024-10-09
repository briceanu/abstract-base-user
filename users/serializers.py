from rest_framework import serializers
from .models import BlogUser
import re
from rest_framework.exceptions import ValidationError

class BlogUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = BlogUser
        fields = ['user_id', 'email', 'username', 'password', 'confirm_password', 'is_married', 'signup_date','age']

    def validate_password(self, value):
        errors = []
        if not re.search(r'[A-Z]', value):
            errors.append('Password must contain at least one uppercase letter.')
        if len(value) < 8:
            errors.append('Password must be at least 8 characters long.')
        if not re.search(r'\d', value):
            errors.append('Password must contain at least one number.')
        if errors:
            raise ValidationError(errors)
        return value

    def validate_age(self,value):
        if value < 18:
            raise ValidationError(detail='Age can not be less than 18 years old')
        return value


    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError({'confirm_password': 'Passwords do not match.'})
        
        # Check if username already exists
        if BlogUser.objects.filter(username=data.get('username')).exists():
            raise ValidationError({'username': 'Username already exists.'})
        
        # Check if email already exists
        if BlogUser.objects.filter(email=data.get('email')).exists():
            raise ValidationError({'email': 'Email already exists.'})
        
        return data 

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = BlogUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
