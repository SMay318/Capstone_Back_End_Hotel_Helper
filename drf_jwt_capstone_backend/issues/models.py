from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Issues(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=50)
    severity_rating = models.IntegerField(default=0, null=False)
    status_pending = models.BooleanField(default=False)
    status_completed = models.BooleanField(default=False)


