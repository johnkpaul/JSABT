from django.shortcuts import render_to_response;
from django.template import RequestContext;
from photocopy.models import Photocopy
from django.core import serializers
from django.http import HttpResponse
import feedparser

def home(request):
    results = Photocopy.objects.all()[:5]
    return render_to_response('home.html', {'results': results},context_instance=RequestContext(request))

def bookmarks(request):
    return render_to_response('photocopy/bookmarks.html',context_instance=RequestContext(request));

def search(request, search_query):
    results = list(Photocopy.objects.filter(article_content__icontains=search_query))
    results_as_json = serializers.serialize('json', results, fields=('title','url','description'))
    response = HttpResponse(results_as_json,mimetype='application/json')
    return response

def load(request):
    feed_url = request.GET['feed']
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        p = Photocopy();
        p.title = entry.title
        p.description = entry.description
        p.url = entry.link
        p.save()
    return HttpResponse("")
