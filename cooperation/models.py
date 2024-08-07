from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, svg_help_text, resize_img


class CooperationPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    image = models.ImageField('Баннер', upload_to=get_file_path, help_text=image_help_text)

    image_1500_webp = models.ImageField(upload_to=get_file_path)
    image_1500_jpg = models.ImageField(upload_to=get_file_path)

    left_text = models.TextField('Текст слева')
    right_text = models.TextField('Текст справа')

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(CooperationPage, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and self.image != self.__original_image:
            self.image_1500_webp = resize_img(self.image_1500_webp, self.image, [1500, 460], 'webp')
            self.image_1500_jpg = resize_img(self.image_1500_jpg, self.image, [1500, 460], 'png')
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Общая страница сотрудничества'

    class Meta:
        verbose_name = 'Общая страница сотрудничества'
        verbose_name_plural = 'Общая страница сотрудничества'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="400">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class Wholesale(models.Model):

    title = models.CharField('Оптовые продажи', max_length=255)
    subtitle = models.TextField('Подзаголовок')

    first_city = models.CharField('Указание города (Бишкек)', max_length=255)
    second_city = models.CharField('Указание города (Ош)', max_length=255)

    first_phone = models.CharField('Телефон (Бишкек)', max_length=255)
    second_phone = models.CharField('Телефон (Ош)', max_length=255)

    def __str__(self):
        return 'Оптовые продажи'

    class Meta:
        verbose_name = 'Оптовые продажи'
        verbose_name_plural = 'Оптовые продажи'


class Retailsale(models.Model):

    title = models.CharField('Розничные продажи', max_length=255)
    subtitle = models.TextField('Подзаголовок')

    first_city = models.CharField('Указание города (Бишкек)', max_length=255)
    second_city = models.CharField('Указание города (Ош)', max_length=255)

    first_phone = models.CharField('Телефон (Бишкек)', max_length=255)
    second_phone = models.CharField('Телефон (Ош)', max_length=255)

    def __str__(self):
        return 'Сотрудничество и предложения'

    class Meta:
        verbose_name = 'Сотрудничество и предложения'
        verbose_name_plural = 'Сотрудничество и предложения'


class Partners(models.Model):

    title = models.CharField('Партнеры', max_length=255)
    subtitle = models.TextField('Подзаголовок')

    def __str__(self):
        return 'Партнеры'

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'


class PartnersItems(models.Model):

    partners = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='partner_items')

    image = models.ImageField('Логотип', upload_to=get_file_path, help_text=image_help_text)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение партнера'
        verbose_name_plural = 'Изображения партнеров'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class CooperationForm(models.Model):

    main_title = models.CharField('Работа в Тойбосс', max_length=255)
    subtitle = models.TextField('Подзаголовок (Хотите расти вместе с нами...)')

    name = models.CharField('Ваше имя', max_length=255)
    phone = models.CharField('Ваш номер', max_length=255)
    position = models.CharField('Желаемая позиция', max_length=255)

    message = models.CharField('Ваше сообщение', max_length=255)

    rules = RichTextField('Условия соглашения', blank=True)

    file = models.CharField('Прикрепить файл', max_length=255)

    send_button = models.CharField('Кнопка "Отправить"', max_length=255)

    def __str__(self):
        return 'Форма (Сотрудничество)'

    class Meta:
        verbose_name = 'Форма (Сотрудничество)'
        verbose_name_plural = 'Форма (Сотрудничество)'


