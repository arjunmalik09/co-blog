from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog/(?P<id>\d+)/desc/$', views.blog_desc, name='blog_desc'),
    url(r'^blog/(?P<id>\d+)/edit/$', views.blog_edit, name='blog_edit'),
    url(r'^blog/create/$',views.blog_create,name='blog_create'),
    url(r'^blog/(?P<id>\d+)/delete/$', views.blog_delete, name='blog_delete'),
]
