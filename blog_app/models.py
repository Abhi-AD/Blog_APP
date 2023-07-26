from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
     published_at = models.DateTimeField(null=True, blank=True)
     
     def __str__(self):
          return self.title