from django.shortcuts import render

# Create your views here.
from parkinginfo.models import Parkinginfo, Comment, User
from parkinginfo.serializers import parkinginfoSerializer, commentSerializer, userSerializer

from rest_framework import viewsets

class parkinginfoViewSet(viewsets.ModelViewSet):
	queryset = Parkinginfo.objects.all()
	serializer_class = parkinginfoSerializer

class commentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = commentSerializer

class userViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = userSerializer