from django.views.generic import DetailView
from .models import Post


class PostDetailView(DetailView):
    model = Post