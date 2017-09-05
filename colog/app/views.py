"""
Definition of views.
"""
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache

from .functions import *
from .models import *
from .forms import *
from .Keywords import Keywords

from random import SystemRandom
from string import ascii_lowercase,digits


from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from operator import itemgetter

sp = "<seperator>"



@never_cache
def user_login(request):
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print user

        # If we have a User object, the details are correct. If None, no user with matching credentials was found.
        if user:
            if user.is_active:           
                login(request, user)
                return redirect('/home/')
            else:
                return HttpResponse("Your account has been deactivated.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.<a href='/home/'>Back To Homepage.</a>")

    else:
        return render(request, 'app/login.html', {})
    return render(request,'app/login.html')

@never_cache
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            
            user = user_form.save(commit=False)
            user.username = user.email.split('@')[0]
            
            print "Registering:",user.username," with pwd ",user.password
            password = ''.join(SystemRandom().choice(ascii_lowercase + digits) for i in range(8))
            user.set_password(password)
            user.save()
            profile = AppUserprofile(id=user.id,picture='default.png')
            profile.save()

            success = send_email(user, password)
            if not success:
                profile.delete()
                user.delete()
                return HttpResponse("Error during registration process.Please retry registering yourself.<br>.<a href='/home/'>Back To Homepage.</a>")

            return HttpResponse("Your account has been registered.Your login details have been sent to your email:"+user.email+" <br>.<a href='/home/'>Back To Homepage.</a>")

        else:
            print user_form.errors

            context = {
                'form': user_form, 
            }
            return render(request, 'app/signup.html',context)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {
            'form': user_form, 
        }
        print context
        return render(request, 'app/signup.html', context)


    # url(r'^blog/(?P<id>[0-9]{1,12})/desc/$', views.blog_desc, name='blog_desc'),
    # url(r'^blog/(?P<id>[0-9]{1,12})/edit/$', views.blog_edit, name='blog_edit'),
    # url(r'^blog/create/$',views.blog_create,name='blog_create'),
    # url(r'^blog/(?P<id>[0-9]{1,12})/delete/$', views.blog_delete, name='blog_delete'),

@never_cache
def main(request):
    
    post_set = Post.objects.all()
    heading_set = []
    rank = []

    for instance in post_set:
        heading = get_object_or_404(User,id = instance.up.id)
        heading_set.append(heading)
        rank.append([instance,heading,get_rank(instance.time,instance.likes)])
        # print type(instance.time)


    rank = sorted(rank, key=itemgetter(2))
    rank.reverse()
    # lt = [{'heading':t[0],'post':t[1]} for t in zip(rank[:][1],rank[0][])]
    context = {
        'request': request, 
        'user': request.user,
        'list':rank,
    }
    
    return render(request, 'app/main.html', context)


@never_cache
def blog_desc(request,id):
    instance = get_object_or_404(Post,pt_id=int(id))
    qa = instance.text.split(sp)
    #print qa
    print qa[13]
    context={
        'qa':qa,
        'up':instance.up.id,
        'heading':instance.title,
        'likes':instance.likes,
        'time':instance.time,
        'by':get_object_or_404(User,id = instance.up.id),
        'tags':HasTags.objects.filter(pt_id=instance.pt_id),
        'experience':get_experience(qa[13])
    }
    return render(request,'app/desc.html',context)


@never_cache
@login_required
def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        q0 = "Which subjects/topics your study/training was about?"
        a0 = request.POST.get("ques0")
        q1 = "Where did you study/get Training?"
        a1 = request.POST.get("ques1")
        q2 = "Why did you choose this field(Background/Initial Motivation)?"
        a2 = request.POST.get("ques2")
        q3 = "How did you get the Fianancial Assistance(Family Conditions/Scholorships)?"
        a3 = request.POST.get("ques3")
        q4 = "How was the training/study/experience?"
        a4 = request.POST.get("ques4")
        q5 = "What did you gain from this activity(skill set) & its impact on your current/future life?"
        a5 = request.POST.get("ques5")
        q6 = "Satisfaction & suggestions for others."
        a6 = request.POST.get("ques6")
        

        up = get_object_or_404(AppUserprofile,id=request.user.id)
        post = Post(text=q0+sp+a0+sp+q1+sp+a1+sp+q2+sp+a2+sp+q3+sp+a3+sp+q4+sp+a4+
            sp+q5+sp+a5+sp+q6+sp+a6,likes=0,up=up,time=str(datetime.datetime.now())[:19],title=title)

        if q1 is not None and q2 is not None and q3 is not None and q4 is not None and q5 is not None and q6 is not None and title is not None:
            tags = get_tags(title + a0 + a5)
            post.save()
            topics = []
            for tag in tags:
                if tag in Keywords:
                    topics.append(tag)
                    topic = Topic(name=tag)
                    topic.save()
                    HasTags(t=topic,pt=post).save()
            
            messages.success(request,"Successfully Created")
            return HttpResponseRedirect(post.get_absolute_url())
            
    context = {}
    return render(request,"app/blog.html",context)


@never_cache
@login_required
def blog_edit(request):
    return render(request,'app/blog.html')

@never_cache
@login_required
def blog_delete(request):
    return render(request,'app/blog.html')

@never_cache
@login_required
def user_logout(request):
    logout(request)
    return redirect('/home/')

@never_cache
def about(request):
    return render(request,'app/about.html')

@never_cache
def contact(request):
    return render(request,'app/contact.html')