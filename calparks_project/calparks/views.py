from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import models
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson as json
from django import http
import datetime
from django.utils import simplejson
from django.conf import settings


from calparks.models import ParkInfo, UserRecommendations 
from calparks.forms import ParkInfoForm, UserRecommendationsForm

class ParkInfoDetail(DetailView):
    context_object_name = "parkinfo_detail"
    model = ParkInfo
    def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        return ctx

class ParkInfoList(ListView):
    context_object_name = "parkinfo_list"
    model = ParkInfo
    print "Called ParkInfoList"
    def get_queryset(self, **kwargs):
        all_entries = ParkInfo.objects.all()
        print all_entries
        return ParkInfo.objects.all()

@login_required
def parkinfo_add(request, id=None, template_name='calparks/parkinfo_form.html'):
    if id:
        parkinfo = get_object_or_404(ParkInfo, id=id)
    else:
        parkinfo = ParkInfo()
    if request.method == 'POST':
        form = ParkInfoForm(request.POST, instance=parkinfo)
        if form.is_valid():
            parkinfo = form.save(commit=False)
            parkinfo.save()
            return HttpResponseRedirect(reverse('parkinfo_list'))
    else:
        form = ParkInfoForm(instance=parkinfo)
    return render(request, template_name, {'form': form})


class UserRecommendationsDetail(DetailView):
    context_object_name = "userrecommendations_detail"
    model = UserRecommendations
    def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        return ctx

class UserRecommendationsList(ListView):
    context_object_name = "userrecommendations_list"
    model = UserRecommendations
    def get_queryset(self, **kwargs):
        kwargs['user'] = self.request.user
        return UserRecommendations.objects.filter(**kwargs)



@login_required
def userrecommendations_add(request, template_name='calparks/userrecommendations_add.html'):
    if request.method == 'POST':
        form = UserRecommendationsForm(request.POST)
        if form.is_valid():
            userrecommendations = form.save(commit=False)
            userrecommendations.user = request.user
            userrecommendations.save()
            return HttpResponseRedirect(reverse('userrecommendations_list' ))
        else:
            print 'Form is not valid....'
    else:
        form = UserRecommendationsForm()
        if form.is_valid():
            userrecommendations = form.save(commit=False)
            userrecommendations.user = request.user
            userrecommendations.save()
        else:
            print 'Form is not valid Error => '
            print form.errors
            print 'Form is not valid non_filed_errrors => '
            print form.non_field_errors

    return render(request, template_name, {'form': form})

