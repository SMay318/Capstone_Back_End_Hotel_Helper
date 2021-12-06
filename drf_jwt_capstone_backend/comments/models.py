from django.db import models
from django.contrib.auth import get_user_model
from issues.models import Issues

User = get_user_model()

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issues,on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
