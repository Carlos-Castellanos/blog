from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(default='AIFA1.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):  ## is executed when a form is used, resolves the error after the POST
        return reverse("post_list")

        #return reverse("pages/home")