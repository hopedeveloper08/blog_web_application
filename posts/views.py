from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.urls import reverse

from taggit.models import Tag

from posts.models import Post
from posts.forms import EmailPostForm, CommentForm


class PostListView(generic.ListView):
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list/list.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')

        if not tag_slug:
            return Post.published.all()

        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = Post.published.filter(tags__in=[tag])
        return object_list


class PostDetailView(generic.DetailView, generic.FormView):
    queryset = Post.published.all()
    context_object_name = 'post'
    template_name = 'detail/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.get_object()

        comments = post.comments.all()
        context['comments'] = comments

        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_post= Post.published \
            .filter(tags__in=post_tags_ids) \
            .distinct() \
            .exclude(id=post.id)
        similar_post = similar_post.annotate(same_tags=Count('tags')) \
            .order_by('-same_tags', '-published_at')[:4]
        context['similar_post'] = similar_post

        return context

    def form_valid(self, form):
        try:
            slug = self.kwargs['slug']
            comment = form.save(commit=False)
            comment.post = Post.objects.get(slug=slug)
            comment.save()
            messages.success(self.request, 'Comment create successfully')
        except:
            messages.error(self.request, 'There was an error to create comment')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Input was invalid')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs=self.kwargs)


class PostShareView(generic.FormView):
    form_class = EmailPostForm
    template_name = 'email/email.html'

    def form_valid(self, form):
        try:
            form.send_email(self.request, self.kwargs['post_id'])
            messages.success(self.request, 'Email sent successfully')
        except:
            messages.error(self.request, 'There was an error sending the email')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Input was invalid')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('posts:post_share', kwargs=self.kwargs)
