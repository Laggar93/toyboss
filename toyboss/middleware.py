from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from toyboss.config import admin_url


class ForceInEnglish(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> None:
        if request.path.startswith('/' + admin_url):
            request.COOKIES[settings.LANGUAGE_COOKIE_NAME] = 'ru'