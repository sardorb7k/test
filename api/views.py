from blog.models import Post
from .serializers import PostSerializer
from rest_framework.generics import *

class UpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer