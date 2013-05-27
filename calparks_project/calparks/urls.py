from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from calparks.views import ParkInfoDetail, ParkInfoList, UserRecommendationsDetail, UserRecommendationsList 
from calparks.forms import ParkInfoForm, UserRecommendationsForm

urlpatterns = patterns('',
    url(r'^park/add/$', 'calparks.views.parkinfo_add', name='parkinfo_add'),
    url(r'^park/list/$', login_required(ParkInfoList.as_view()), name='parkinfo_list'),
    url(r'^park/(?P<id>\d+)/edit/$', 'calparks.views.parkinfo_add', name='parkinfo_edit'),
)
