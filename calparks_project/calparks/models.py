from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

class ParkInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    county = models.CharField(max_length=100,blank=False)
    park_type = models.CharField(max_length=100,blank=True)
    park_size = models.DecimalField(max_digits=10,decimal_places=2,null=True) 
    url = models.CharField(max_length=100,blank=True,null=True) 
    average_user_rec = models.PositiveSmallIntegerField(default=0, null=True)
    class Meta:
        verbose_name = "Park Information"
        verbose_name_plural = "Park Information"
    #So the drop down will show park name
    def __unicode__(self):
        return self.name

class UserRecommendations(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    park = models.ForeignKey(ParkInfo,on_delete=models.PROTECT)
    comments = models.TextField(blank=True, null=True)
    user_rating = models.PositiveSmallIntegerField(default=1,blank=False, null=True)
    rec_timestamp = models.DateTimeField(editable=False, null=True, default=datetime.now)
    class Meta:
        verbose_name = "User Recommendation"
        verbose_name_plural = "User Recommendations"
