from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, resize_img


class NewsPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    other_news_title = models.CharField('Заголовок "Другие новости"', max_length=255)

    button_name = models.CharField('Наименование кнопки', max_length=255)

    def __str__(self):
        return 'Общая страница новостей'

    class Meta:
        verbose_name = 'Общая страница новостей'
        verbose_name_plural = 'Общая страница новостей'


class NewsItem(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    news_title = models.CharField('Заголовок новости', max_length=255)

    text = RichTextField('Текст', blank=True)

    published = models.DateField('Дата публикации', auto_now_add=False, null=True, editable=True)

    slug = models.SlugField('URL', max_length=50, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = make_slug(self.slug, self.news_title, NewsItem, self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsSlider(models.Model):

    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name='news_images', verbose_name='Изображение')

    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)

    image_1499_webp = models.ImageField(upload_to=get_file_path)
    image_1499_jpg = models.ImageField(upload_to=get_file_path)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(NewsSlider, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and self.image != self.__original_image:
            self.image_1499_webp = resize_img(self.image_1499_webp, self.image, [1499, 576], 'webp')
            self.image_1499_jpg = resize_img(self.image_1499_jpg, self.image, [1499, 576], 'jpeg')

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новости'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


