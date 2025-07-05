from django import template
import re

register = template.Library()

@register.filter(name='add_class_to_p')
def add_class_to_p(html):
    # 1. Добавить класс к <p>
    def add_class(match):
        tag = match.group(0)
        if 'class="' in tag:
            tag = re.sub(r'class="([^"]*)"', r'class="\1 news-block-card-desc"', tag)
        else:
            tag = re.sub(r'<p', '<p class="news-block-card-desc"', tag)
        return tag

    html = re.sub(r'<p[^>]*>', add_class, html)

    # 2. Найти все <p ...> теги и убедиться, что у каждого есть </p>
    # Найти все теги <p ...>
    p_tags = list(re.finditer(r'<p[^>]*>', html))
    closed_positions = [m.start() for m in re.finditer(r'</p>', html)]

    result = ''
    last_index = 0
    for p_tag in p_tags:
        start = p_tag.start()
        end = p_tag.end()
        result += html[last_index:start]

        open_tag = html[start:end]
        content_start = end

        # Найдём следующий <p или </p> или конец строки
        next_close = re.search(r'</p>', html[content_start:])
        next_open = re.search(r'<p[^>]*>', html[content_start:])

        if next_close and (not next_open or next_close.start() < next_open.start()):
            close_index = content_start + next_close.end()
            content = html[content_start:close_index]
            result += open_tag + content
            last_index = close_index
        else:
            # Закрывающий тег не найден — закрываем вручную
            if next_open:
                content = html[content_start:content_start + next_open.start()]
                last_index = content_start + next_open.start()
            else:
                content = html[content_start:]
                last_index = len(html)
            result += open_tag + content + '</p>'

    result += html[last_index:]
    return result
