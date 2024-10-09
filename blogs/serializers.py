from rest_framework import serializers
from .models import BlogModel
from rest_framework.validators import ValidationError


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields =  ['username', 'details', 'age', 'id']


    def validate_age(self,value):
        if value < 18:
            raise ValidationError(detail='Age can not  be less than 18 years old.')
        if value > 65:
            raise ValidationError(detail='Age can not be older than 65 years old.')
        return value
            
    
    def validate_details(self,value):
        forbiden_characters = ['`','&','||','|','&&']
        for char in forbiden_characters:
            if char in value:
                raise ValidationError(detail='These characters are not allowed: `, &, ||, |, &&')
        return value
            