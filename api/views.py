from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response


class PostListView(views.APIView):
    def get(self, request, format=None):
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostDetailView(views.APIView):
    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response()


class CommentView(views.APIView):
    def post(self, request, format=None):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)