"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
#from .functions import n_day_hence
import datetime
from django.core.urlresolvers import reverse

class AppUserprofile(models.Model):
    dob = models.DateField(blank=True, null=True)
    mobile_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    education_place = models.CharField(max_length=40, blank=True, null=True)
    education_field = models.CharField(max_length=40, blank=True, null=True)
    employment_place = models.CharField(max_length=40, blank=True, null=True)
    employment_designation = models.CharField(max_length=40, blank=True, null=True)
    occupation = models.CharField(max_length=40, blank=True, null=True)
    residence_place = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    picture = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_userprofile'

class Post(models.Model):
    pt_id = models.AutoField(primary_key=True)
    text = models.TextField()
    likes = models.IntegerField()
    up = models.ForeignKey(AppUserprofile)
    time = models.DateTimeField()
    title = models.CharField(max_length=140)

    def get_absolute_url(self):
		# return reverse("app:blog_desc",kwargs={"id":self.pt_id})
		return '/home/blog/'+str(self.pt_id)+'/desc/'

    class Meta:
        managed = False
        db_table = 'post'

class Comment(models.Model):
    c_id = models.AutoField(primary_key=True)
    text = models.TextField()
    likes = models.IntegerField()
    pt = models.ForeignKey('Post')

    class Meta:
        managed = False
        db_table = 'comment'

class Follows(models.Model):
    f_id = models.AutoField(primary_key=True)
    up_id_follower = models.ForeignKey(AppUserprofile, db_column='up_id_follower',related_name='follower')
    up_id_following = models.ForeignKey(AppUserprofile, db_column='up_id_following',related_name='following')

    class Meta:
        managed = False
        db_table = 'follows'


class Topic(models.Model):
    name = models.CharField(max_length=120)
    t_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'topic'


class HasInterest(models.Model):
    h_i_id = models.AutoField(primary_key=True)
    up = models.ForeignKey(AppUserprofile)
    t = models.ForeignKey('Topic')

    class Meta:
        managed = False
        db_table = 'has_interest'


class HasTags(models.Model):
    h_t_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey('Post')
    t = models.ForeignKey('Topic')

    class Meta:
        managed = False
        db_table = 'has_tags'

# # Create your models here.
# class UserProfile(models.Model) :

#     # one to one association with User Model
#     user = models.OneToOneField(User)

#     # variables specific to Registration Model
#     dob = models.DateField()
#     mobile_no = models.CharField(unique=True, max_length=20)
#     education_place = models.CharField(max_length=40)
#     education_field = models.CharField(max_length=40)
#     employment_place = models.CharField(max_length=40)
#     employment_designation = models.CharField(max_length=40)
#     occupation = models.CharField(max_length=40)
#     residence_place = models.CharField(max_length=60)
#     country = models.CharField(max_length=30)
#     picture = models.ImageField(upload_to='profile_images', blank=True)

#     def __unicode__(self) :
#         return str(self.user.username)

# # Create your models here.
# class UserInterests(models.Model) :

#     # one to one association with User Model
#     user = models.OneToOneField(User)

#     # variables specific to Registration Model
#     interest = models.CharField(max_length=60)
# 	user = models.ForeignKey('UserProfile')

#     def __unicode__(self) :
#         return str(self.roll_no)

# # Create your models here.
# class user_profile(models.Model) :

#     # one to one association with User Model
#     user = models.OneToOneField(User)

#     # variables specific to Registration Model
# 	aadhar_card_no = models.ForeignKey('UserProfile', db_column='aadhar_card_no')
#     roll_no = models.CharField(primary_key=True,max_length=10,null=False)
#     passing_year = models.IntegerField(default=(str(datetime.date.today())).split('-')[0],null=False)
#     course = models.CharField(choices=course_type, default='BTECH', null=False,max_length=5)
#     department = models.CharField(choices=department_type, default='CER', null=False,max_length=4)
#     alternative_email = models.EmailField(max_length=120,unique=True)
#     account_type = models.CharField(default='Student Account', null=False,max_length=20)

#     def __unicode__(self) :
#         return str(self.roll_no)
