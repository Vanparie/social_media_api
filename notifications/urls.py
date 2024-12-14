# notifications/urls.py

from django.urls import path
from notifications.views import NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
