from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, svg_help_text, resize_img


class ProductionPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    youtube_link = models.URLField('Ссылка на Youtube')

    def __str__(self):
        return 'Общая страница производства'

    class Meta:
        verbose_name = 'Общая страница производства'
        verbose_name_plural = 'Общая страница производства'


class Advantages(models.Model):

    main_title = models.CharField('Заголовок', max_length=255)

    first_advantage = models.CharField('Первое преимущество', max_length=255)
    second_advantage = models.CharField('Второе преимущество', max_length=255)
    third_advantage = models.CharField('Третье преимущество', max_length=255)
    fourth_advantage = models.CharField('Четвертое преимущество', max_length=255)
    fifth_advantage = models.CharField('Пятое преимущество', max_length=255)
    sixth_advantage = models.CharField('Шестое преимущество', max_length=255)

    def __str__(self):
        return 'Преимущества'

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'


class Points(models.Model):

    order = models.IntegerField('Порядок')

    point_title = models.CharField('Заголовок', max_length=255)

    icon = models.FileField('Иконка', upload_to=get_file_path, help_text=svg_help_text,
                            validators=[FileExtensionValidator(['svg'])])

    text = RichTextField('Текст')

    def __str__(self):
        return self.point_title

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class PointsSlider(models.Model):

    point = models.ForeignKey(Points, on_delete=models.CASCADE, related_name='points_slider', verbose_name='Пункт')

    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)

    image_735_webp = models.ImageField(upload_to=get_file_path)
    image_735_jpg = models.ImageField(upload_to=get_file_path)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(PointsSlider, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and self.image != self.__original_image:
            self.image_735_webp = resize_img(self.image_735_webp, self.image, [735, 561], 'webp')
            self.image_735_jpg = resize_img(self.image_735_jpg, self.image, [735, 561], 'jpeg')

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение в слайдере'
        verbose_name_plural = 'Изображения в слайдере'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'






