from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['email'], email=validated_data['email'], password=validated_data['password'])
        return user

from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
    
    
from rest_framework import serializers
from .models import Model1

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Accept dynamic fields during initialization
        fields = kwargs.pop('fields', None)
        super(Model1Serializer, self).__init__(*args, **kwargs)

        if fields is not None:
       
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def update(self, instance, validated_data):
        # Update only the fields that are provided
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    
    
    
class GetModel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        exclude = ['id']  # Exclude the id field
