from rest_framework import serializers
from .models import Issues

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['id', 'issue_name', 'description', 'category', 'severity_rating', 'status_pending', 'status_completed', 'user_id']