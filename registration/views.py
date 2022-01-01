from django.shortcuts import render
from django.contrib.auth.models import User
from registration.serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.

class  SignUp(CreateAPIView):
    permission_class= []
    authentication_classes = []
    serializer_class= RegistrationSerializer
    queryset= User.objects.all()
