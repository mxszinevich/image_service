from io import BytesIO
from typing import Tuple
from urllib import request

from PIL import Image

from django.core.files.base import ContentFile
from django.core.files.images import ImageFile


def create_path_image_data(instance, name: str) -> str:
    """
    Функция формирования пути к изображению
    """
    return f"{name}"


def get_modified_size_image(image_data: dict, image) -> Tuple[int, int]:
    """
    Функция, возвращающая размер изображения
    """
    width = image_data.get("width") or image.width
    height = image_data.get("height") or image.height

    return int(width), int(height)


def get_resize_image(image_data: dict, image) -> ContentFile:
    """
    Функция, возращающая необработанный (raw) фаил
    """
    new_image = Image.open(image.picture)
    image_format = new_image.format
    new_image = new_image.resize(get_modified_size_image(image_data, image))
    buffer = BytesIO()
    new_image.save(fp=buffer, format=image_format)

    return ContentFile(buffer.getvalue())


def get_image_from_url(url: str):
    """
    Функция загрузки изображения по url
    """
    content = request.urlretrieve(url)
    image = ImageFile(open(content[0], "rb"))
    return image


def get_image_name(url: str):
    """
    Метод формирующий имя изображения по url
    """
    return url.split("/")[-1]
