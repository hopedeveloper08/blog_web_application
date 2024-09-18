from django.shortcuts import get_object_or_404
from django.views import generic

from posts.models import Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.published.all()
    template_name = 'post_list.html'


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
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
