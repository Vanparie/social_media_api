from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Get unread notifications for the current user
        return Notification.objects.filter(recipient=self.request.user, read=False)

