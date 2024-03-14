from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name = BlogConfig.name


urlpatterns = [
    path("create/", PostCreateView.as_view(), name="create"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
