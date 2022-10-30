from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentForm
from blog.models import Post, Comment


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('category_slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        # создаем контекст, передаем аргументы
        context = super().get_context_data(**kwargs)
        # добавляем в контекст form
        context['form'] = CommentForm
        # возвращаем контекст
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return self.object.post.get_absolute_url()


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'