from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
  title = models.CharField(max_length=300)
  description = models.CharField(max_length=5000)
  image = models.ImageField(blank=True, null=True, upload_to="upload")
  writer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title