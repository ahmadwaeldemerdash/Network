from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import User, Post, Follow


def index(request):
    posts = Post.objects.all().order_by("-time")
    p = Paginator(posts, 10)
    page = request.GET.get("page")
    posts = p.get_page(page)
    return render(request, "network/index.html", {
        "posts" : posts
    })
def following(request):
    user = User.objects.get(username=request.user)
    users = []
    f = Follow.objects.all().filter(follower=user)
    for i in f.values():
        user = i['followed_id']
        user = User.objects.get(pk=user)
        users.append(user)
    posts = []
    for user in users:
       user = User.objects.get(username=user)
       post = Post.objects.all().filter(user=user)
       posts.extend(post)
    p = Paginator(posts, 10)
    page = request.GET.get("page")
    posts = p.get_page(page)  
    return render(request, "network/index.html",{
        "posts" : posts,
        "token" : 1,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def create_post(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text == "":
            message = "Please Enter a Valid Input!"
            return render(request, "network/new_post.html",{
                "message" : message
            })
        post = Post(user=request.user,text=text)
        post.save()
        url = reverse("index")
        print(url)
        return HttpResponseRedirect(url)

    return render(request, 'network/new_post.html')
def profile(request, name):
    token = 0
    user = User.objects.get(username=name)
    posts = Post.objects.all().filter(user=user).order_by("-time")
    follows = Follow.objects.all().filter(follower=user.id).count()
    followed_by = Follow.objects.all().filter(followed=user.id).count()
    try:
        Follow.objects.get(follower=request.user.id, followed=user.id)  
        token = 1
    except:
        print("")
    return render(request, "network/profile.html",{
        "posts": posts,
        "user": user,
        "follows": follows,
        "followed_by": followed_by ,
        "token": token
    })
     
def follow(request):
    if request.method == "POST":
        if request.POST.get("follow") is not None:
            followed_user = User.objects.get(username=request.POST.get("follow"))
            follower = User.objects.get(username=request.user)
            db = Follow(follower=follower, followed=followed_user)
            db.save()
            user_name = request.POST.get("follow")
            url = reverse("profile", args=[user_name])
            return HttpResponseRedirect(url)
        else:
            followed = request.POST.get("unfollow")
            followed_user = User.objects.get(username=followed)
            follower = request.user.id
            db = Follow.objects.get(follower=follower, followed=followed_user)  
            db.delete()
            url = reverse("profile", args=[followed])
            return HttpResponseRedirect(url)
@csrf_exempt
def change_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'PUT': 
        data = json.loads(request.body)
        if data.get('likes') is not None and data.get('likes') > 0: 
            post.likes += data['likes']  
            post.save()
        if data.get('content') is not None and data.get('content') != "":
            post.text = data['content']
            post.save()
        return HttpResponse(status=204)
        
    elif request.method == 'GET':
        return JsonResponse(post.serialize())


