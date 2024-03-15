# from django.shortcuts import render
from blog.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy("blog:post_list")


class PostListView(ListView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy("blog:post_list")

