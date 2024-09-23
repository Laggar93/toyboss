from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, svg_help_text, resize_img
from django.utils.safestring import mark_safe


class ProductCategory(models.Model):

    order = models.IntegerField('Порядок')

    category_title = models.CharField('Наименование категории', max_length=255)

    sandwich_mark = models.BooleanField('Галочка для категории сэндвичей', blank=True, default=False)

    chicken_mark = models.BooleanField('Галочка для куриного мяса', default=False, blank=True,)

    slug = models.SlugField('URL', max_length=50, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = make_slug(self.slug, self.category_title, ProductCategory, self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_title

    class Meta:
        ordering = ['order']
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'


class Products(models.Model):

    order = models.IntegerField('Порядок')

    product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category_products', verbose_name='Категория')

    product_title = models.CharField('Наименование продукта', max_length=255)

    description = models.TextField('Описание', blank=True)
    compound = models.TextField('Состав', blank=True)

    fact = models.TextField('Факт', blank=True)

    image_semismocked = models.ImageField('Изображение 239 x 306 (полукопченая колбаса)', upload_to=get_file_path, help_text=image_help_text, blank=True)
    image_boiled = models.ImageField('Изображение 274 x 331 (вареная колбаса)', upload_to=get_file_path, help_text=image_help_text, blank=True)
    image_chicken = models.ImageField('Изображение 185 x 267 (куриное мясо)', upload_to=get_file_path, help_text=image_help_text, blank=True)
    image_sausages = models.ImageField('Изображение 199 x 251 (сосиски)', upload_to=get_file_path, help_text=image_help_text, blank=True)

    image_detail = models.ImageField('Детальное изображение продукции', upload_to=get_file_path, help_text=image_help_text, blank=True)


    main_show = models.BooleanField('Отобразить на главной странице', default=False, blank=True)
    catalog_show = models.BooleanField('Отобразить на странице продукции (каталога)', default=True, blank=True)


    slug = models.SlugField('URL', max_length=50, allow_unicode=True, unique=True, blank=True)

    first_image_animation = models.ImageField('Первое изображение анимации', upload_to=get_file_path, help_text=image_help_text, blank=True)
    second_image_animation = models.ImageField('Второе изображение анимации', upload_to=get_file_path, help_text=image_help_text, blank=True)
    third_image_animation = models.ImageField('Третье изображение анимации', upload_to=get_file_path, help_text=image_help_text, blank=True)

    __original_image_semismocked = None


    __original_first_image_animation = None
    __original_second_image_animation = None
    __original_third_image_animation = None

    def __init__(self, *args, **kwargs):
        super(Products, self).__init__(*args, **kwargs)

        self.__original_image_semismocked = self.image_semismocked

        self.__original_image_boiled = self.image_boiled

        self.__original_image_chicken = self.image_chicken

        self.__original_image_sausages = self.image_sausages

        self.__original_image_detail = self.image_detail


        self.__original_first_image_animation = self.first_image_animation
        self.__original_second_image_animation = self.second_image_animation
        self.__original_third_image_animation = self.third_image_animation

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = make_slug(self.slug, self.product_title, Products, self.id)

        if self.image_semismocked and self.image_semismocked != self.__original_image_semismocked:
            self.image_semismocked = resize_img(self.image_semismocked, self.image_semismocked, [239, 306], 'png', 'transparent')

        if self.image_boiled and self.image_boiled != self.__original_image_boiled:
            self.image_boiled = resize_img(self.image_boiled, self.image_boiled, [274, 331], 'png', 'transparent')

        if self.image_chicken and self.image_chicken != self.__original_image_chicken:
            self.image_chicken = resize_img(self.image_chicken, self.image_chicken, [185, 267], 'png', 'transparent')

        if self.image_sausages and self.image_sausages != self.__original_image_sausages:
            self.image_sausages = resize_img(self.image_sausages, self.image_sausages, [199, 251], 'png', 'transparent')

        if self.image_detail and self.image_detail != self.__original_image_detail:
            self.image_detail = resize_img(self.image_detail, self.image_detail, [300, 452], 'png', 'transparent')


        if self.first_image_animation and self.first_image_animation != self.__original_first_image_animation:
            self.first_image_animation = resize_img(self.first_image_animation, self.first_image_animation, [241, 451], 'png', 'transparent')

        if self.second_image_animation and self.second_image_animation != self.__original_second_image_animation:
            self.second_image_animation = resize_img(self.second_image_animation, self.second_image_animation, [243, 495], 'png', 'transparent')

        if self.third_image_animation and self.third_image_animation != self.__original_third_image_animation:
            self.third_image_animation = resize_img(self.third_image_animation, self.third_image_animation, [266, 370], 'png', 'transparent')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_title

    class Meta:
        ordering = ['order']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @cached_property
    def display_image_semismocked(self):
        return format_html('<img src="{img}" width="200">', img=self.image_semismocked.url)
    display_image_semismocked.short_description = 'Предпросмотр изображения 239 x 306'

    @cached_property
    def display_image_boiled(self):
        return format_html('<img src="{img}" width="200">', img=self.image_boiled.url)
    display_image_boiled.short_description = 'Предпросмотр изображения 274 x 331'

    @cached_property
    def display_image_chicken(self):
        return format_html('<img src="{img}" width="200">', img=self.image_chicken.url)
    display_image_chicken.short_description = 'Предпросмотр изображения 185 x 267'

    @cached_property
    def display_image_sausages(self):
        return format_html('<img src="{img}" width="200">', img=self.image_sausages.url)
    display_image_sausages.short_description = 'Предпросмотр изображения 199 x 251'

    @cached_property
    def display_image_detail(self):
        return format_html('<img src="{img}" width="200">', img=self.image_detail.url)
    display_image_detail.short_description = 'Предпросмотр изображения 300 x 452'

    @cached_property
    def display_first_image_animation(self):
        return format_html('<img src="{img}" width="200">', img=self.first_image_animation.url)
    display_first_image_animation.short_description = 'Предпросмотр первого изображения анимации'

    @cached_property
    def display_second_image_animation(self):
        return format_html('<img src="{img}" width="200">', img=self.second_image_animation.url)
    display_second_image_animation.short_description = 'Предпросмотр второго изображения анимации'

    @cached_property
    def display_third_image_animation(self):
        return format_html('<img src="{img}" width="200">', img=self.third_image_animation.url)
    display_third_image_animation.short_description = 'Предпросмотр третьего изображения анимации'

    def image_tag(self):
        if self.image_semismocked:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_semismocked.url)
        if self.image_boiled:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_boiled.url)
        if self.image_chicken:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_chicken.url)
        if self.image_sausages:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_sausages.url)
        else:
            return 'Изображение не найдено'
    image_tag.short_description = 'Изображение продукта'

    def image_tag_detail(self):
        if self.image_detail:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_detail.url)

    image_tag_detail.short_description = 'Детальное изображение продукта'


class ProductPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    def __str__(self):
        return 'Общая страница продуктов'

    class Meta:
        verbose_name = 'Общая страница продуктов'
        verbose_name_plural = 'Общая страница продуктов'


