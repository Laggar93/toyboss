from ckeditor.fields import RichTextField
from django.db import models
from toyboss.functions import resize_img, get_file_path, image_help_text
from django.utils.html import format_html
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe


class MainPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    def __str__(self):
        return 'Общая страница'

    class Meta:
        verbose_name = 'Общая страница'
        verbose_name_plural = 'Общая страница'


class MainPageSlider(models.Model):

    order = models.IntegerField('Порядок')

    title = models.CharField('Заголовок', max_length=255, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255, blank=True)
    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)
    image_webp = models.ImageField(upload_to=get_file_path)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(MainPageSlider, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and self.image != self.__original_image:
            self.image = resize_img(self.image, self.image, [1920, 1080], 'jpeg')
            self.image_webp = resize_img(self.image_webp, self.image, [1920, 1080], 'webp')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'Главный слайдер'
        verbose_name_plural = 'Главный слайдер'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'


class Groups(models.Model):

    title = models.CharField('Заголовок', max_length=255)

    sandwich_text = models.TextField('Текст сэндвичей')
    toyboss_text = models.TextField('Текст колбасы')
    agrokush_text = models.TextField('Текст Агрокуша')
    broiler_text = models.TextField('Текст Кыргыз Бройлера')

    def __str__(self):
        return 'Группа компаний'

    class Meta:
        verbose_name = 'Группа компаний'
        verbose_name_plural = 'Группа компаний'


class MainProd(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    top_text = models.TextField('Текст сверху')
    bottom_text = models.TextField('Текст снизу')

    def __str__(self):
        return 'Производство'

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'


class MainProdSlider(models.Model):

    main_page = models.ForeignKey(MainProd, on_delete=models.CASCADE, related_name='main_prod_slider')

    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(MainProdSlider, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and self.image != self.__original_image:
            self.image = resize_img(self.image, self.image, [1920, 1080], 'jpeg')
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Слайдер производства'
        verbose_name_plural = 'Слайдер производства'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class MainCooperation(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    subtitle = models.TextField('Подзаголовок')

    first_city = models.CharField('Указание города (Бишкек)', max_length=255)
    second_city = models.CharField('Указание города (Ош)', max_length=255)

    first_phone = models.CharField('Телефон (Бишкек)', max_length=255)
    second_phone = models.CharField('Телефон (Ош)', max_length=255)

    def __str__(self):
        return 'Сотрудничество'

    class Meta:
        verbose_name = 'Сотрудничество'
        verbose_name_plural = 'Сотрудничество'


class Survey(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    button_name = models.CharField('Наименование кнопки', max_length=255)
    link = models.URLField('Ссылка на гугл форму')

    def __str__(self):
        return 'Опрос'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опрос'


class MainQuote(models.Model):

    history_title = models.CharField('Заголовок истории', max_length=255)
    history_text = models.TextField('Текст истории')

    mission_title = models.CharField('Заголовок миссии', max_length=255)
    mission_text = RichTextField('Текст миссии')

    value_title = models.CharField('Заголовок ценности', max_length=255)
    value_text = models.TextField('Текст ценности')

    first_line = models.CharField('Первая строка', max_length=255)
    second_line = models.CharField('Вторая строка', max_length=255)
    third_line = models.CharField('Вторая строка', max_length=255)

    first_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255)

    def __str__(self):
        return 'История, миссия и ценности'

    class Meta:
        verbose_name = 'История, миссия и ценности'
        verbose_name_plural = 'История, миссия и ценности'




