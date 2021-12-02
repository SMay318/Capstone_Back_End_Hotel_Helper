from django.urls import path
from issues import views

urlpatterns = [
    path('all/', views.get_all_issues),
    path('', views.user_issues)
]