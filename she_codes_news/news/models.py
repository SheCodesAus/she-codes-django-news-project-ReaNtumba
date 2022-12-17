from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER,on_delete=models.CASCADE,
        related_name="stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(max_length = 1000, default="https://images.unsplash.com/photo-1475518845976-0fd87b7e4e5d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Z3JlZW4lMjBza3l8ZW58MHx8MHx8&w=1000&q=80")
    favourited_by = models.ManyToManyField(USER, related_name="favourites", blank=True)
    