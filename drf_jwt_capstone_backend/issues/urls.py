from django.urls import path
from drf_jwt_capstone_backend.issues.views import IssuesDetail
from issues import views

urlpatterns = [
    path('', views.IssuesList.as_view()),
    path('<int:pk>', views.IssuesDetail.as_view()),
]