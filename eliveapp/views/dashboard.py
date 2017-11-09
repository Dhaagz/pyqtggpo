from django.shortcuts import get_object_or_404,render
from eliveapp.models import Channel
from django.contrib.auth.decorators import login_required
import logging
from eliveapp.hashutils import HashUtils

@login_required
def dashboard(request):
    logger = logging.getLogger('elive')
    u = request.user
    logger.debug("dashboard %s : affichage" %u.username)
    channel = get_object_or_404(Channel, title=u.username)
    return render(request, 'eliveapp/dashboard.html', {'channel': channel})

@login_required
def generate_key(request):
    u = request.user
    logger = logging.getLogger('elive')
    logger.debug("dashboard %s : generation d'une clef de streaming" %u.username)
    channel = get_object_or_404(Channel, title=u.username)
    new_key = HashUtils.random_channel_key()
    channel.key = new_key
    channel.save()
    return render(request, 'eliveapp/dashboard.html', {'channel': channel})

@login_required
def set_topic(request):
    u = request.user
    logger = logging.getLogger('elive')
    logger.debug("dashboard %s : definition d'un nouveau topic" %u.username)
    channel = get_object_or_404(Channel, title=u.username)
    channel.topic = request.topic
    channel.save()
    return render(request, 'eliveapp/dashboard.html', {'channel': channel})
