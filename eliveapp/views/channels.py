from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from eliveapp.models import Channel
import logging
from django.contrib.auth.decorators import login_required
from eliveapp.hashutils import HashUtils

def channel(request, channel_title):
    channel = get_object_or_404(Channel, title=channel_title)
    return render(request, 'eliveapp/channel.html', {'channel': channel})

def check_publish_url(request):
    logger = logging.getLogger('django')
    input_channelkey = request.GET.get('st');
    channel_title = request.GET.get('name');
    status_code = 501
    logger.debug("check url : st = %s name = %s" %(input_channelkey,channel_title))

    if not(input_channelkey is None or channel_title is None):
        channel = get_object_or_404(Channel, title=channel_title)
        logger.debug("channel récupérée : clé %s" %channel.key)
        #Check key is valid and different from db placeholder key
        if input_channelkey == channel.key and channel.key != "unset_key":
            status_code = 200

    return HttpResponse(status=status_code)

