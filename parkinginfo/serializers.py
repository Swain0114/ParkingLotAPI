from rest_framework import serializers
from parkinginfo.models import Parkinginfo, Comment, User

class parkinginfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parkinginfo
		fields = '__all__'

class commentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'