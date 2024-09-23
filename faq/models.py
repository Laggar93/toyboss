from ckeditor.fields import RichTextField
from django.db import models


class FaqPage(models.Model):

    title = models.CharField('Заголовок SEO', max_length=1000)
    description = models.TextField('Описание SEO', blank=True)
    keywords = models.TextField('Ключевые слова SEO', blank=True)

    page_title = models.CharField('Заголовок страницы', max_length=255)

    link = models.URLField('Ссылка на опросник')

    main_button = models.CharField('Все вопросы (кнопка на главной странице)', max_length=255)

    def __str__(self):
        return 'Общая страница часто задаваемых вопросов'

    class Meta:
        verbose_name = 'Общая страница часто задаваемых вопросов'
        verbose_name_plural = 'Общая страница часто задаваемых вопросов'


class Questions(models.Model):

    question = models.TextField('Вопрос')
    answer = RichTextField('Ответ')
    show_main_page = models.BooleanField('Отображать на главной странице', default=False, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'


