from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=2)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
