from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, resize_img


class AboutPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    def __str__(self):
        return 'Общая страница О нас'

    class Meta:
        verbose_name = 'Общая страница О нас'
        verbose_name_plural = 'Общая страница О нас'


class History(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(History, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and self.image != self.__original_image:
            self.image = resize_img(self.image, self.image, [730, 504], 'jpeg')

        super().save(*args, **kwargs)

    def __str__(self):
        return 'История'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class Years(models.Model):

    year = models.CharField('Год', max_length=255)
    description = RichTextField('Текст')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Годы'


class Mission(models.Model):

    title = models.CharField('Заголовок', max_length=255)

    quote = models.CharField('Цитата', max_length=255)
    text = models.TextField('Текст')

    def __str__(self):
        return 'Миссия'

    class Meta:
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссия'


class Vision(models.Model):

    title = models.CharField('Заголовок', max_length=255)

    text = models.TextField('Текст')

    def __str__(self):
        return 'Видение'

    class Meta:
        verbose_name = 'Видение'
        verbose_name_plural = 'Видение'


class Value(models.Model):

    title = models.CharField('Заголовок', max_length=255)

    text = models.TextField('Верхний текст')

    def __str__(self):
        return 'Ценности'

    class Meta:
        verbose_name = 'Ценности'
        verbose_name_plural = 'Ценности'


class ValuePoints(models.Model):

    first_title = models.CharField('Доверие потребителя (заголовок)', max_length=255)
    first_text = models.TextField('Доверие потребителя (описание)')

    second_title = models.CharField('Мы - это люди (заголовок)', max_length=255)
    second_text = models.TextField('Мы - это люди (описание)')

    third_title = models.CharField('На шаг впереди (заголовок)', max_length=255)
    third_text = models.TextField('На шаг впереди (описание)')

    fourth_title = models.CharField('Вклад в общество (заголовок)', max_length=255)
    fourth_text = models.TextField('Вклад в общество (описание)')

    fifth_title = models.CharField('Прозрачная и честная деятельность (заголовок)', max_length=255)
    fifth_text = models.TextField('Прозрачная и честная деятельность (описание)')

    def __str__(self):
        return 'Пункты ценностей'

    class Meta:
        verbose_name = 'Пункты ценностей'
        verbose_name_plural = 'Пункты ценностей'


class StatisticPoints(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    left_postscript = models.CharField('Приписка слева', max_length=255, blank=True)
    number = models.CharField('Число', max_length=255)
    right_postscript = models.CharField('Приписка справа', max_length=255, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункты статистики'
        verbose_name_plural = 'Пункты статистики'


class Statistic(models.Model):

    title = models.CharField('Заголовок', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Certificates(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    button_name = models.CharField('Название кнопки', max_length=255)

    def __str__(self):
        return 'Сертификаты'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class CertificatesItems(models.Model):

    certificates = models.ForeignKey(Certificates, related_name='cert_images', on_delete=models.CASCADE)

    cert_image = models.ImageField('Сертификат', upload_to=get_file_path, help_text=image_help_text)
    title = models.CharField('Заголовок', max_length=255, blank=True)
    description = models.TextField('Текст', blank=True)

    # __original_image = None
    #
    # def __init__(self, *args, **kwargs):
    #     super(CertificatesItems, self).__init__(*args, **kwargs)
    #     self.__original_image = self.cert_image
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.cert_image and self.cert_image != self.__original_image:
    #         self.cert_image = resize_img(self.cert_image, self.cert_image, [184, 260])
    #     super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение сертификата'
        verbose_name_plural = 'Изображения сертификата'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.cert_image.url)
    display_image.short_description = 'Предпросмотр изображения'


class Rewards(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    button_name = models.CharField('Название кнопки', max_length=255)

    def __str__(self):
        return 'Награды'

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'


class RewardsItems(models.Model):

    rewards = models.ForeignKey(Rewards, related_name='rewards_images', on_delete=models.CASCADE)

    reward_image = models.ImageField('Награда', upload_to=get_file_path, help_text=image_help_text)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение награды'
        verbose_name_plural = 'Изображения награды'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.reward_image.url)
    display_image.short_description = 'Предпросмотр изображения'






