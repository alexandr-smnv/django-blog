from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('category_slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'