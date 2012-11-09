from django.shortcuts import render_to_response

def index(request):
    return render_to_response('{{ app_name }}.html', locals(), context_instance=RequestContext(request))
