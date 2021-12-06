from django.urls import path
from comments import views


urlpatterns = [
  path('', views.CommentsList.as_view()),
  path('<int:pk>', views.CommentsDetail.as_view())
]