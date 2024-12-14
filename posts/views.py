from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#posts/views.py (Enhanced)

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    ...
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']



# Implement the Feed Functionality


from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from posts.serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        """
        Return posts from users the current user is following, ordered by creation date.
        """
        # Get the users the current user is following
        following_users = request.user.following.all()

        # Filter posts where the author is in the list of following users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Order by most recent first
        
        # Serialize the posts and return the response
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')



# Implement LIKE functionality

# posts/views.py

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404  # Import get_object_or_404
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        post = get_object_or_404(Post, pk=pk)  # Retrieve the post using get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)  # Get or create a Like
        generics.get_object_or_404(Post, pk=pk)

        # Prevent user from liking a post multiple times
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create like and notification
        like = Like.objects.create(user=user, post=post)

        # Create notification for the post owner
        notification = Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post,
        )

        return Response({"detail": "Post liked successfully!"}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        return Response({"detail": "Post unliked successfully!"}, status=status.HTTP_200_OK)



class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])  # Use get_object_or_404 here
        return post