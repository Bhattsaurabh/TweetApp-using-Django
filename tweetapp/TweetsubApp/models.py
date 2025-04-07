from django.db import models
from django.contrib.auth.models import User



class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #current admin user
    text = models.TextField(max_length=250)
    photo = models.ImageField(upload_to='photos/', blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'


class RepostTweet(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)         #current admin user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user.username} reposted {self.tweet.text}'
