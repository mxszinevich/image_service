from django.db import models

from image_service.utils import create_path_image_data, get_image_from_url


class ImageData(models.Model):
    """
    Модель хранения изображений
    """

    name = models.CharField(verbose_name="Название изображения", max_length=300)
    url = models.URLField(
        verbose_name="Ссылка на изображение", max_length=500, blank=True, null=True
    )
    picture = models.ImageField(
        verbose_name="Изображение", upload_to=create_path_image_data, blank=True, null=True
    )
    width = models.PositiveIntegerField(verbose_name="Ширина изображения", blank=True, null=True)
    height = models.PositiveIntegerField(verbose_name="Высота изображения", blank=True, null=True)
    parent_picture = models.ForeignKey(
        "self",
        verbose_name="Родительское изображение",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def save(self, *args, **kwargs):
        if self.url and not self.picture:
            self.picture.save(self.name, get_image_from_url(self.url), save=False)

        if self.picture:
            self.width = self.picture.width
            self.height = self.picture.height
            self.name = self.picture.name

        super().save(*args, **kwargs)
