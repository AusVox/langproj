from django.template.defaulttags import register
# register = template.Library()


@register.filter
def index(indexable, i):
    """Позволяет использовать answers|index:forloop.counter0 в quiz.html
    для обращения к элементам списка по индексу"""
    return indexable[i]