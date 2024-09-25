from django import template
from django.utils.safestring import mark_safe

from markdown import markdown

from posts.models import Post


register = template.Library()


@register.inclusion_tag('list/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-published_at')[:count]
    return {'latest_posts': latest_posts}


@register.filter(name='markdown')
def markdown_formatted(text):
    return mark_safe(markdown(text))
