from rest_framework import serializers
from .models import CNNImage


class CNNImageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNNImage
        fields = ['id','name','submitted_as_meme','image','meme_confidence','no_meme_confidence','correct_prediction']


class CNNImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNNImage
        fields = ['id','name','submitted_as_meme','image']
