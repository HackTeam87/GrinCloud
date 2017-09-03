from django.conf.urls import url
from blog import views


from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    #url(r'^cat$', views.post_list, name='post_list'),
    #url(r'^cat$', views.post_list, name='winter'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editor, name='post_edit'),
    #url(r'^home/$', views.home, name='home'),
    #url(r'^$', views.home2, name='home2'),
    #url(r'^(?P<slug>[-\w]+)/cat/$', views.category, name='cat'),
    #url(r'^kat/(?P<slug>[-\w]+)$', views.category, name='cat'),
    #url(r'^$', views.ind, name='ind'),
    #url(r'^car$', views.carusel, name='car'),
	url(r'^dz1$', views.dz1, name='dz1'),
    url(r'^dz2$', views.dz2, name='dz2'),
    #url(r'^circle$', views.circle, name='circle'),
    #url(r'^grid$', views.grid, name='grid'),




    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editor, name='post_edit'),
    #url(r'^home/$', views.home, name='home'),
    #url(r'^home2/$', views.home2, name='home2'),
    #url(r'^(?P<slug>[-\w]+)/$', views.category, name='cat'),



]