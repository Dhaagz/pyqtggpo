from eliveapp.models import Channel
from django.shortcuts import render

def index(request):
    channel_list = Channel.objects.order_by('-title')[:50]
    context = {'channel_list': channel_list}
    #output = ', '.join([c.title for c in channel_list])
    return render(request, 'eliveapp/index.html', context)
