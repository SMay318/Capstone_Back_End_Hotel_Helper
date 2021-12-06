from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comments
from .serializers import CommentsSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes({AllowAny})
def get_all_comments(request):
    comments = Comments.objects.all()
    serializer = CommentsSerializer(comments, many =True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_comments(request):

    print('User', f"{request.user.id}{request.user.email}{request.user.username}")

    if request.method == 'POST':
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errrors, status=status.HTTP_400_BAD_REquest)
    elif request.method == 'GET':
        issues = Comments.objects.filter(user_id=request.user.id)
        serializer = CommentsSerializer(issues, many=True)
        return Response(serializer.data)
