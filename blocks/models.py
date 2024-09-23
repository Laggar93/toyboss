from django.db import models
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text


class NavigationMenu(models.Model):

    about = models.CharField('О нас', max_length=255)
    production = models.CharField('Производство', max_length=255)
    product = models.CharField('Продукция', max_length=255)
    cooperation = models.CharField('Сотрудничество', max_length=255)
    news = models.CharField('Новости', max_length=255)
    contact = models.CharField('Контакты', max_length=255)
    faq = models.CharField('FAQ', max_length=255)

    ustukan_game_general = models.CharField('Игра Устукан', max_length=255)
    ustukan_game_first = models.CharField('Игра Устукан (все еще в разработке) (первое предложение)', max_length=255, blank=True)
    ustukan_game_second = models.CharField('Игра Устукан (все еще в разработке) (второе предложение)', max_length=255, blank=True)

    def __str__(self):
        return 'Панель навигации'

    class Meta:
        verbose_name = 'Панель навигации'
        verbose_name_plural = 'Панель навигации'


class Footer(models.Model):

    title = models.CharField('Заголовок под логотипом', max_length=255)
    rights = models.CharField('Заголовок (все права защищены)', max_length=255)
    whatsup_number = models.CharField('Номер Whatsapp', max_length=255)

    office_title = models.CharField('Заголовок (Офис в г. Бишкек)', max_length=255)
    address = models.CharField('Заголовок (Адрес)', max_length=255)

    phone_title = models.CharField('Заголовок (телефон)', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)

    email = models.EmailField('Email')

    def __str__(self):
        return 'Футер'

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class NotFound(models.Model):

    page_not_found_first = models.CharField('Страница не найдена', max_length=255)
    page_not_found_second = models.CharField('Страница, на которую вы пытаетесь попасть, не существует или была удалена', max_length=255)
    to_main = models.CharField('На главную', max_length=255)
    image = models.ImageField('Изображение', upload_to=get_file_path, help_text=image_help_text)

    def __str__(self):
        return '404'

    class Meta:
        verbose_name = '404'
        verbose_name_plural = '404'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="200">', img=self.image.url)
    display_image.short_description = 'Предпросмотр изображения'


class GeneralTranslations(models.Model):

    detail_button = models.CharField('Кнопка "Подробнее"', max_length=255)
    product_description = models.CharField('Описание (продукты)', max_length=255)
    product_compound = models.CharField('Состав (продукты)', max_length=255)
    product_all = models.CharField('Все (продукты, главная страница)', max_length=255)

    def __str__(self):
        return 'Общие переводы'

    class Meta:
        verbose_name = 'Общие переводы'
        verbose_name_plural = 'Общие переводы'
