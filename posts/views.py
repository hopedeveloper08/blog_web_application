from django.views import generic

from posts.models import Post


class PostListView(generic.ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post_list.html'


class PostDetailView(generic.DetailView):
    queryset = Post.published.all()
    context_object_name = 'post'
    template_name = 'post_detail.html'
