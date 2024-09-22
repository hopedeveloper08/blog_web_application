from django import template

from posts.models import Post


register = template.Library()


@register.inclusion_tag('list/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-published_at')[:count]
    return {'latest_posts': latest_posts}
