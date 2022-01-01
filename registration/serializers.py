from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    password= serializers.CharField(write_only=True)
    password2= serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


    def validate(self, data):
        password= data.get('password')
        password2= data.get('password2')
        email= data.get('email')
        username= data.get('username')

        if password != password2:
            raise serializers.ValidationError("Password does not match")
        else:
            return data

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("User with {} already exists".format(value))
        else:
            return value




    def create(self, validated_data):
        username= validated_data.get('username')
        first_name= validated_data.get('first_name')
        last_name= validated_data.get('last_name')
        email= validated_data.get('email')
        password= validated_data.get('password')
        user= User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return user
