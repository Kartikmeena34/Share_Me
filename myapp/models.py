from django.db import models

# Create your models here.
import uuid
from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional if you want user management

    def __str__(self):
        return f"File {self.id}"