from django.db import models

# Create your models here.
class Comment(models.Model):
    blog_post = models.CharField(max_length = 20, null =False)
    comment_text = models.TextField(null = False)
    author = models.CharField(max_length = 100, default = "anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(name = "approved",default=False)
    
    def __str__(self):
        return str(self.blog_post) + " " + str(self.author)