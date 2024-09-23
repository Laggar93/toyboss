import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from toyboss import config

SECRET_KEY = config.secret_key
DEBUG = config.debug
ALLOWED_HOSTS = config.hosts

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'adminsortable2',
    'django_unused_media',
    'news.apps.NewsConfig',
    'faq.apps.FaqConfig',
    'contacts.apps.ContactsConfig',
    'cooperation.apps.CooperationConfig',
    'product.apps.ProductConfig',
    'production.apps.ProductionConfig',
    'about.apps.AboutConfig',
    'main.apps.MainConfig',
    'blocks.apps.BlocksConfig',
    'news.templatetags.custom_tags'
]

MIDDLEWARE = [
    'toyboss.middleware.ForceInEnglish',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toyboss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'toyboss.context_processors.globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'toyboss.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '4f0vl1et5cf.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


gettext = lambda s: s

# Обновление LANGUAGES для использования 'kg' вместо 'ky'
LANGUAGES = (
    ('ky', gettext('Kyrgyz')),
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)

# Обновление EXTRA_LANG_INFO для использования 'kg' вместо 'ky'
EXTRA_LANG_INFO = {
    'ky': {
        'bidi': False,
        'code': 'ky',
        'name': 'Kyrgyz',
        'name_local': u"Кыргызча",
    },
}

import django.conf.locale
from django.conf import global_settings

# Объединение новой информации о языке с существующими данными LANG_INFO
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

# Обновление глобальных настроек языков
global_settings.LANGUAGES = global_settings.LANGUAGES + [("ky", 'Кыргызча')]

import os
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

# Убедитесь, что пути локалей настроены корректно
LOCALE_PATHS = (
    os.path.join(PACKAGE_ROOT, 'locale'),
)

# Обновление конфигурации MODELTRANSLATION_LANGUAGES для использования 'kg'
MODELTRANSLATION_LANGUAGES = ('ru', 'ky', 'en')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'


STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'toyboss/static/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'allowedContent': True,
        'toolbar_Custom': [
            ['BulletedList'],
            ['Source'],
        ]
    },
}



EMAIL_HOST = config.mail_host
EMAIL_PORT = config.mail_port
EMAIL_HOST_USER = config.mail_login
EMAIL_HOST_PASSWORD = config.mail_password
EMAIL_USE_TLS = config.mail_use_tls




