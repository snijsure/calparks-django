from django.conf import settings
from django.contrib.sites.models import Site


def globals(request):
    data = {}
    current_site = Site.objects.get_current()

    data.update({
        'site': current_site,
    })
    return data
