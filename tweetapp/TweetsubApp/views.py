from django.shortcuts import render
from .forms import TweetForm, UserRegistrationForm
from .models import Tweet
from django.shortcuts import get_object_or_404, redirect   #ORM to interact with DB
from django.contrib.auth.decorators import login_required  #decorators are  used for tasks like authentication, authorization, or caching
from django.contrib.auth import login

# Create your views here.


def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets} )


@login_required             #(Login authentication) it makes sure that user is loged in before going to create a tweet 
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)    # not save form in DB
            tweet.user = request.user       # har request m user hota hi h
            tweet.save()        # commit = false ni h toh form DB m save hoga
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form' : form})
    

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form' : form})
    

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet' : tweet})
    


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)    # not save form in DB
            user.set_password(form.cleaned_data(['password1']))
            user.save()        # commit = false ni h toh form DB m save hoga
            login(request, user)  #automatically logged in user
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form' : form})
