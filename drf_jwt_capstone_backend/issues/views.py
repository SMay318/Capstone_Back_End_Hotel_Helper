from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Issues
from .serializers import IssuesSerializer
from django.contrib.auth.models import User

class IssuesList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        issues = Issues.objects.all()
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data)

