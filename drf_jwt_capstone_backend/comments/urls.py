from django.urls import path
from comments import views

urlpatterns = [
    path('allComments/', views.get_all_comments),
    path('createComment/', views.user_comments),
]