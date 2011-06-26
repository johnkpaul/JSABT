from django.shortcuts import render_to_response;
from django.template import RequestContext;
from photocopy.models import Photocopy
from django.core import serializers
from django.http import HttpResponse

def home(request):
    return render_to_response('home.html',context_instance=RequestContext(request));

def search(request, search_query):
    print search_query
    results = list(Photocopy.objects.filter(article_content__icontains=search_query))
    results_as_json = serializers.serialize('json', results, fields=('title','url','description'))
    response = HttpResponse(results_as_json,mimetype='application/json')
    return response
