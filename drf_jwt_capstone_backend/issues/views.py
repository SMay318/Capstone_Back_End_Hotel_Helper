from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Issues
from .serializers import IssuesSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes({AllowAny})
def get_all_issues(request):
    issues = Issues.objects.all()
    serializer = IssuesSerializer(issues, many =True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_issues(request):

    print('User', f"{request.user.id}{request.user.email}{request.user.username}")

    if request.method == 'POST':
        serializer = IssuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errrors, status=status.HTTP_400_BAD_REquest)
    elif request.method == 'GET':
        issues = Issues.objects.filter(user_id=request.user.id)
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data)

@api_view({'GET', 'PUT','DELETE'})
@permission_classes({IsAuthenticated})
def issue_details(request):
    issues= Issues.objects.filter(user_id=request.user.id)
    serializer = IssuesSerializer(issues, many=True)
    if request.method == 'GET':
        serializer = IssuesSerializer(issues)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssuesSerializer(issues, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issues.delete()
        return Response ({'Alert': 'Issue was successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)

