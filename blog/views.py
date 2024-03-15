# from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from blog.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pytils.translit import slugify


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object



class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'preview')
    # success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:details', args=[self.kwargs.get('pk')])


def published_activity(request, pk):
    post_item = get_object_or_404(Post, pk=pk)
    if post_item.published:
        post_item.published = False
    else:
        post_item.published = True
    post_item.save()
    return redirect(reverse_lazy('blog:post_list'))
