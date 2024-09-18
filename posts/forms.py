from django import forms
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from posts.models import Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_email(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, is_published=True)
        post_url = request.build_absolute_uri(post.get_absolute_url())
        subject = f'{self.cleaned_data["name"]} recommends you read {post.title}'
        message = f'Read {post.title} at {post_url}\n\n' \
                  f'{self.cleaned_data["name"]}\'s comments {self.cleaned_data["comments"]}'
        send_mail(
            subject,
            message,
            self.cleaned_data["email"],
            (self.cleaned_data['to'],),
        )
