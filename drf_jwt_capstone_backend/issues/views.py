from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Issues
from .serializers import IssuesSerializer
from rest_framework.permissions import IsAuthenticated


class IssuesList(APIView):

    def get(self, request):
        issues = Issues.objects.all()
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IssuesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssuesDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Issues.objects.get(pk=pk)
        except Issues.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        issue = self.get_object(pk)
        serializer = IssuesSerializer(issue)
        return Response(serializer.data)

    def put(self, request, pk):
        update_issue = self.get_object(pk)
        serializer = IssuesSerializer(update_issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_issue = self.get_object(pk)
        delete_issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


