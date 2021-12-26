from rest_framework import serializers

from image_service.models import ImageData


class ImageDataSerializer(serializers.ModelSerializer):
    """
    Сериализатор изображений (ImageData)
    """
    class Meta:
        model = ImageData
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': False}
        }

