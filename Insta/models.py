from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
    upload_to = 'static/images/profiles',
    format = 'JPEG',
    options = {'quality':100},
    blank = True,
    null = True
    )
    def get_absolute_url(self):
        return reverse("login")
   

class Post(models.Model):
    author =models.ForeignKey(InstaUser, on_delete = CASCADE, related_name = 'my_posts')
    title = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )


    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("posts")
    


class Like(models.Model):
    post = models.ForeignKey(
           Post,
           on_delete=CASCADE ,
           related_name = 'likes'
    )
    user = models.ForeignKey(
           InstaUser, 
           on_delete=CASCADE,
           related_name = 'likes'
    )
    class Meta:
        unique_together =("post","user")
    