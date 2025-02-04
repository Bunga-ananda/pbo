from django.contrib.auth.models import User
from django.db import models

class AdminSistem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    verified = models.BooleanField(default=True)

    def __str__(self):
        return f"Admin: {self.user.username}"

