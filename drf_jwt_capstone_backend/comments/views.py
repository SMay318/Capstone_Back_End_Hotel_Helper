from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CommentsList(APIView):

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        update_comment = self.get_object(pk)
        serializer = CommentsSerializer(update_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_comment = self.get_object(pk)
        delete_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)