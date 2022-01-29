from ast import Or
from datetime import date
from typing import Type
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile , Post , Comment , Like , UserFollowing,Message
import json
from django.db.models import Q,Count
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        user_following = UserFollowing.objects.filter(user_id=user)
        users =[]
        for x in user_following:
            users.append(x.following_user_id) 
        dc ={}
        post = Post.objects.filter(user_name__in = users).order_by('-date_posted')
        # post = Post.objects.all().order_by('-date_posted')
        for x in post:
            try:
                like = Like.objects.get(user=user , post=x)
                dc[x] = 'true'
                    
            except:
                dc[x] = 'false'

        user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)

        return render(request, 'explore.html',{'post':dc,'user_to_follow':user_to_follow})
    else:
        return render(request,'home.html')

def explore(request):
    return render(request,'explore.html')

def trending(request):
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        user_following = UserFollowing.objects.filter(user_id=user)
        users =[]
        for x in user_following:
            users.append(x.following_user_id) 
        posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')  
        dc ={}
        for x in posts:
            try:
                like = Like.objects.get(user=user,post=x)
                dc[x] = 'true'
            except:
                dc[x] = 'false'
        user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)

        return render(request,'trending.html',{'posts':dc,'user_to_follow':user_to_follow})


def search(request):
    if request.GET.get('search'):
        keyword = request.GET['search']
        user =User.objects.all()
        found_users = []
        for i in user:
            if keyword == i.username or i.first_name == keyword:
                found_users.append(i)
                print(found_users)
        return render(request , "search_results.html" , {'users':found_users})

def post(request):
    id = request.user.id
    user = User.objects.get(id = id)   
    des = request.POST['des']
    if 'post_image' in request.FILES:
        image = request.FILES['post_image']   
        post = Post.objects.create(user_name = user , description = des ,img = image)
    else:
        post = Post.objects.create(user_name = user , description = des)
    post.save()
    return redirect('/')
        
def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    user = post.user_name
    return HttpResponse( user)

def comment(request,pk):    
    if request.method == "POST":
        id = request.user.id
        post = Post.objects.get(pk = pk)
        user = User.objects.get(id = id)
        comment_data = request.POST['comment']
        comment = Comment.objects.create(post = post , username = user , comment = comment_data)
        comment.save()
        return HttpResponse('done')
        
def like(request,pk):
    id = request.user.id
    usr = User.objects.get(id=id)
    post = Post.objects.get(pk=pk)
    liked = False
    try:
        like = Like.objects.get(user=usr , post=post).delete()

    except:
        liked = True
        like = Like.objects.create(user=usr , post=post)
        like.save()
    res = {
        'liked':liked
    }
    response = json.dumps(res)
    return HttpResponse(response,content_type="application/json")

def follow_user(request,username):
    id = request.user.id
    usr = User.objects.get(id = id)
    usr2 = User.objects.get(username = username)
    try:
        obj = UserFollowing.objects.get(user_id = usr , following_user_id = usr2).delete()
    except:
        obj = UserFollowing.objects.create(user_id = usr , following_user_id = usr2)
        obj.save()
    
    return redirect('/')
