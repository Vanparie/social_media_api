# notifications/serializers.py

from rest_framework import serializers
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Display the actor's username
    recipient = serializers.StringRelatedField()  # Display the recipient's username
    target = serializers.SerializerMethodField()  # Display target object info

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'recipient', 'verb', 'target', 'timestamp', 'read']

    def get_target(self, obj):
        if obj.target:
            return str(obj.target)  # Return the string representation of the target
        return None
