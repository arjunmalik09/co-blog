from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group,User
from django.shortcuts import render,get_object_or_404
from django.utils import timezone

import httplib, urllib, base64
from json import JSONEncoder
from json import JSONDecoder

from time import time
import math
import datetime

now = datetime.datetime.now(timezone.utc)

def get_rank(t,likes,Comment_mean=0,tags=0,gender='female'):
    kk=0.0
    time = (t-datetime.datetime.now(timezone.utc)).total_seconds()
    # print time
    # time = (t-datetime.datetime(1970,1,1)).total_seconds()
    # time = t.total_seconds()
    if(likes>0):
        kk=kk+math.log(likes,2)
    kk=kk+(time/10000.0)
    kk=kk+Comment_mean*2 + tags*2 +10000
    if gender=='female':
        kk = kk + 2.6;
    print kk
    return kk


def send_email(user, password):

	print "Sending Email:"
	mail_title = 'Welcome to Colog!'
	message = 'Hi '+user.first_name+'. Kindly verify by logging in using your username '+user.username+' and password '+password+'.\n\nRegards\nColog Team\n' 
	print message

	if send_mail(mail_title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False):
		print "Email Sent"
		return True
		# get_object_or_404(Group,name='Company To Verify').user_set.remove(user)
		# get_object_or_404(Group,name='Company Head').user_set.add(user)
	else:
		print "Error Sending Email"
		return False



def get_experience(text="My name is Robin Chawla. I study in Computer Science and Engineering in Banaras Hindu Unversity. I cracked IIT-JEE with rank 912 in year 2014. I was very happy at that time"):
    body={
      "documents": [
        {
          "id": "abcd",
          "text": text
        }
      ]
    }

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '183f71b817464e95a22f669bcfad216e',
    }

    strng=JSONEncoder().encode(body)

    params = urllib.urlencode({
    })
    experience="Internet Problem."
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, strng, headers)
        response = conn.getresponse()
        data = response.read()
        

        newdict=JSONDecoder().decode(data)
        L=newdict["documents"][0]["score"]
        if(L<=0.15):
            experience="Worst"
        elif(L<=0.3):
            experience="Bad"
        elif(L<=0.5):
            experience="Average"
        elif(L<=0.75):
            experience="Good"
        else:
            experience="Wonderful"
            
        conn.close()
    except Exception as e:
        print("Internet Connection Error")
    return experience



def get_tags(text="My name is Robin Chawla. I study in Computer Scince and Engineering in Banaras Hindu Unversity. I cracked IIT-JEE with rank 912 in year 2014. I was very happy at that time"):
    body={
      "documents": [
        {
          "id": "abcd",
          "text": text
        }
      ]
    }

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '183f71b817464e95a22f669bcfad216e',
    }

    strng=JSONEncoder().encode(body)

    params = urllib.urlencode({
    })
    L = []
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, strng, headers)
        response = conn.getresponse()
        data = response.read()
        
       # print(data)

        newdict=JSONDecoder().decode(data)
       # print(newdict)
        L=newdict["documents"][0]["keyPhrases"]
        
        conn.close()
    except Exception as e:
        print("Internet Connection Error")
    return L

