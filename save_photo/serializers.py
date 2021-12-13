from rest_framework import serializers

from save_photo.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image1', 'image2')
