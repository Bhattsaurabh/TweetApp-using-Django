from django.contrib import admin
from .models import Tweet, RepostTweet


# Register your models here.

admin.site.register(Tweet)
admin.site.register(RepostTweet)