from django.shortcuts import render
from django.http import HttpResponse
from eloboost.models import Rank

def boostme(request):
    rank_list = Rank.objects.order_by('price')[:50]
    context = {'rank_list': rank_list}
    #output = ', '.join([c.title for c in channel_list])
    return render(request, 'eloboost/boostme.html', context)
