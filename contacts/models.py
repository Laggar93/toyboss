from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.functional import cached_property
from toyboss.functions import get_file_path, image_help_text, make_slug, svg_help_text


class ContactsPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    page_subtitle = models.TextField('Подзаголовок страницы')

    def __str__(self):
        return 'Общая страница контактов'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class SocialNetwork(models.Model):

    page_title = models.CharField('Заголовок', max_length=255)

    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'


class SocialItems(models.Model):

    social_network = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, related_name='social_items')

    icon = models.FileField('Иконка социальной сети', upload_to=get_file_path, help_text=svg_help_text,
                            validators=[FileExtensionValidator(['svg'])])
    link = models.URLField('Ссылка социальной сети')

    def __str__(self):
        return 'Иконки и ссылки социальных сетей'

    class Meta:
        verbose_name = 'Иконки и ссылки социальных сетей'
        verbose_name_plural = 'Иконки и ссылки социальных сетей'


class Schedule(models.Model):

    schedule_title = models.CharField('График работы', max_length=255)

    monday_friday = models.CharField('Понедельник - пятница', max_length=255)
    monday_friday_hours = models.CharField('Часы работы в понедельник - пятница', max_length=255)
    dinner = models.CharField('Обед', max_length=255)
    dinner_hours = models.CharField('Часы работы в обед', max_length=255)

    def __str__(self):
        return 'График работы'

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'


class MarketingDepartment(models.Model):

    marketing_department_title = models.CharField('Отдел маркетинга', max_length=255)

    marketing_department_email = models.EmailField('Email')
    marketing_department_phone = models.CharField('Телефон', max_length=255)

    def __str__(self):
        return 'Предложения и обратная связь'

    class Meta:
        verbose_name = 'Предложения и обратная связь'
        verbose_name_plural = 'Предложения и обратная связь'


class ProductionDepartment(models.Model):

    production_department_title = models.CharField('Отдел производства', max_length=255)

    production_department_email = models.EmailField('Email')
    production_department_phone = models.CharField('Телефон', max_length=255)

    def __str__(self):
        return 'Отдел кадров'

    class Meta:
        verbose_name = 'Отдел кадров'
        verbose_name_plural = 'Отдел кадров'


class Accounting(models.Model):

    accounting_department_title = models.CharField('Бухгалтерия', max_length=255)

    accounting_department_email = models.EmailField('Email')
    accounting_department_phone = models.CharField('Телефон', max_length=255)

    def __str__(self):
        return 'По другим вопросам'

    class Meta:
        verbose_name = 'По другим вопросам'
        verbose_name_plural = 'По другим вопросам'


class CentralOffice(models.Model):

    central_office_title = models.CharField('Центральный офис', max_length=255)
    central_office_address = models.TextField('Адрес центрального офиса')

    def __str__(self):
        return 'Производственный завод и главный офис'

    class Meta:
        verbose_name = 'Производственный завод и главный офис'
        verbose_name_plural = 'Производственный завод и главный офис'


class CorporateOffice(models.Model):

    corporate_office_title = models.CharField('Корпоративный офис', max_length=255)
    corporate_office_address = models.TextField('Адрес корпоративного офиса')

    def __str__(self):
        return 'Офис отдела продаж и маркетинга'

    class Meta:
        verbose_name = 'Офис отдела продаж и маркетинга'
        verbose_name_plural = 'Офис отдела продаж и маркетинга'


class ContactForm(models.Model):

    main_title = models.CharField('Остались вопросы', max_length=255)
    subtitle = models.TextField('Подзаголовок (Задайте интересующий вас вопрос...)')

    name = models.CharField('Ваше имя', max_length=255)
    email = models.CharField('Ваш email', max_length=255)
    phone = models.CharField('Ваш номер', max_length=255)
    message = models.CharField('Ваше сообщение', max_length=255)

    rules = RichTextField('Условия соглашения', blank=True)

    send_button = models.CharField('Кнопка "Отправить"', max_length=255)

    def __str__(self):
        return 'Форма (Контакты)'

    class Meta:
        verbose_name = 'Форма (Контакты)'
        verbose_name_plural = 'Форма (Контакты)'