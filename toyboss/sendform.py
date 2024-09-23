import re
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from toyboss.config import send_email, send_coop_email


def send_form(name, email, phone, text):
    name = re.sub('<[^<]+?>', '', name)
    email = re.sub('<[^<]+?>', '', email)
    phone = re.sub('<[^<]+?>', '', phone)
    text = re.sub('<[^<]+?>', '', text)

    body = f'<p>Имя: {name}</p><p>Email: {email}</p><p>Телефон: <a href="tel:{phone}">{phone}</a></p><p>Сообщение: {text}</p>'
    send_msg = EmailMessage('Сообщение с сайта toyboss', body, settings.EMAIL_HOST_USER, send_email)
    send_msg.content_subtype = "html"
    send_msg.send()

    return HttpResponse('')


def send_coop_form(name, phone, position, text, file=None):
    name = re.sub('<[^<]+?>', '', name)
    phone = re.sub('<[^<]+?>', '', phone)
    position = re.sub('<[^<]+?>', '', position)
    text = re.sub('<[^<]+?>', '', text)

    body = f'<p>Имя: {name}</p><p>Телефон: <a href="tel:{phone}">{phone}</a></p><p>Желаемая позиция: {position}</p><p>Сообщение: {text}</p>'
    send_msg = EmailMessage('Сообщение с сайта toyboss', body, settings.EMAIL_HOST_USER, send_coop_email)
    send_msg.content_subtype = "html"
    if file:
        send_msg.attach(file.name, file.read(), file.content_type)
    send_msg.send()

    return HttpResponse('')