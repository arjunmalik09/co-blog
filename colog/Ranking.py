from time import time
import math

def fun(likes,Comment_mean,tags):
    kk=0.0

    if(likes>0):
        kk=kk+math.log(likes,2)
    kk=kk+time()/10000.0
    kk=kk+Comment_mean*2 + tags*2

    return kk

