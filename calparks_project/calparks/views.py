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
from django.db.models import Avg
from django.db.models import Sum
import math

from calparks.models import ParkInfo, UserRecommendations 
from calparks.forms import ParkInfoForm, UserRecommendationsForm

from django.db.models.query import QuerySet
from pprint import PrettyPrinter

def dprint(object, stream=None, indent=1, width=80, depth=None):
    """
    A small addition to pprint that converts any Django model objects to dictionaries so they print prettier.

    h3. Example usage

        >>> from toolbox.dprint import dprint
        >>> from app.models import Dummy
        >>> dprint(Dummy.objects.all().latest())
         {'first_name': u'Ben',
          'last_name': u'Welsh',
          'city': u'Los Angeles',
          'slug': u'ben-welsh',
    """
    # Catch any singleton Django model object that might get passed in
    if getattr(object, '__metaclass__', None):
        if object.__metaclass__.__name__ == 'ModelBase':
            # Convert it to a dictionary
            object = object.__dict__
    
    # Catch any Django QuerySets that might get passed in
    elif isinstance(object, QuerySet):
        # Convert it to a list of dictionaries
        object = [i.__dict__ for i in object]
        
    # Pass everything through pprint in the typical way
    printer = PrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)

class ParkInfoList(ListView):
    context_object_name = "parkinfo_list"
    model = ParkInfo
    def get_queryset(self, **kwargs):
        all_entries = ParkInfo.objects.all()
        return ParkInfo.objects.all()

class ParkInfoDetail(DetailView):
    context_object_name = "parkinfo_detail"
    model = ParkInfo
    def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        return ctx

@login_required
def parkinfo_reviews(request, pk ):
    pkinfo = ParkInfo.objects.filter(id = pk)
    reviews = UserRecommendations.objects.filter(park__id=pk)
    template_name='calparks/parkinfo_detail.html'
    return render(request, template_name, {'pkinfo':pkinfo, 'reviews':reviews })


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
        return UserRecommendations.objects.filter(user__username=self.request.user)



@login_required
def userrecommendations_add(request, template_name='calparks/userrecommendations_add.html'):
    if request.method == 'POST':
        form = UserRecommendationsForm(request.POST)
        if form.is_valid():
            park = request.POST['park']
            allParkEntries = UserRecommendations.objects.filter(park__id=park)
            avg = allParkEntries.aggregate(Avg('user_rating'))
            intAvg = avg['user_rating__avg']
            print intAvg
#            avgRec = UserRecommendations.objects.filter(park__id=park).aggregate(Avg(user_rating))
            userrecommendations = form.save(commit=False)
            userrecommendations.user = request.user
            userrecommendations.save()
            ParkInfo.objects.filter(id=park).update(average_user_rec=intAvg)
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
