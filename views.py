from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    return render_to_response('{{ app_name }}.html', locals(), context_instance=RequestContext(request))
