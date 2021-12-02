from django.urls import path
from issues import views

urlpatterns = [
    path('', views.IssuesList.as_view())
]