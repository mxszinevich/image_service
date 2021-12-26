from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from image_service.api.serializers import ImageDataSerializer
from image_service.models import ImageData
from image_service.utils import get_resize_image


class ImageDataView(viewsets.ModelViewSet):
    """
    Представление для работы с изображениями (ImageData)
    """
    queryset = ImageData.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ImageDataSerializer
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        url = self.request.data.get('url')
        serializer_data = {}
        if url is not None:
            if self.request.data.get('name') is None:
                serializer_data['name'] = self.get_image_name(url)
        serializer.save(**serializer_data)

    def get_image_name(self, url):
        """
        Метод формирующий имя изображения по url
        """
        return url.split('/')[-1]

    @action(detail=True, methods=['post'],  url_path='resize')
    def resize(self, request, **kwargs):
        """
        Изменение размера изображение
        """
        image = get_object_or_404(ImageData, pk=kwargs.get('pk'))
        modified_image = get_resize_image(image_data=self.request.data, image=image)
        image.picture.save(image.picture.name, modified_image)
        serializer = ImageDataSerializer(image)
        return Response(serializer.data)


















