from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from posts.models import Post


class PostListView(generic.TemplateView):
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        posts = Post.published.all()
        paginator = Paginator(posts, 3)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return {
            'posts': posts,
            'page': page,
        }


class PostDetailView(generic.TemplateView):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(
            Post,
            is_published=True,
            slug=self.kwargs['slug'],
            published_at__year=self.kwargs['year'],
            published_at__month=self.kwargs['month'],
            published_at__day=self.kwargs['day'],
        )
        return {'post': post}
