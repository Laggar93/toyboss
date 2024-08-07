from django import template
import re

register = template.Library()

@register.filter(name='add_class_to_p')
def add_class_to_p(html):
    def add_class(match):
        tag = match.group(0)
        if 'class="' in tag:
            tag = re.sub(r'class="([^"]*)"', r'class="\1 news-block-card-desc"', tag)
        else:
            tag = re.sub(r'<p', '<p class="news-block-card-desc"', tag)
        return tag

    modified_html = re.sub(r'<p[^>]*>', add_class, html)
    return modified_html
