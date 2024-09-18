from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.urls import reverse

from posts.models import Post
from posts.forms import EmailPostForm


class PostListView(generic.ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list/list.html'


class PostDetailView(generic.DetailView):
    queryset = Post.published.all()
    context_object_name = 'post'
    template_name = 'detail/detail.html'


class PostShareView(generic.FormView):
    form_class = EmailPostForm
    template_name = 'email/email.html'

    def form_valid(self, form):
        try:
            form.send_email(self.request, self.kwargs['post_id'])
            messages.success(self.request, 'Email sent successfully')
        except Exception as e:
            print(e)
            messages.error(self.request, 'There was an error sending the email')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error sending the email')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('posts:post_share', kwargs={'post_id': self.kwargs['post_id']})
