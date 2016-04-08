#from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from calparks.views import ParkInfoDetail, ParkInfoList, UserRecommendationsDetail, UserRecommendationsList 
from calparks.forms import ParkInfoForm, UserRecommendationsForm
from django.conf.urls import patterns
from django.conf.urls import url



urlpatterns = patterns('',
    url(r'^park/add/$', 'calparks.views.parkinfo_add', name='parkinfo_add'),
    url(r'^park/list/$', login_required(ParkInfoList.as_view()), name='parkinfo_list'),
    url(r'^park/list/(?P<pk>\d+)/$', 'calparks.views.parkinfo_reviews', name='parkinfo_reviews'),
    url(r'^park/(?P<id>\d+)/edit/$', 'calparks.views.parkinfo_add', name='parkinfo_edit'),

    url(r'^review/add/$', 'calparks.views.userrecommendations_add', name='userrecommendations_add'),
    url(r'^review/list/$', login_required(UserRecommendationsList.as_view()), name='userrecommendations_list'),
    url(r'^review/(?P<id>\d+)/(?P<park>\d+)/edit/$', 'calparks.views.userrecommendations_add', name='userrecommendations_edit'),
)
