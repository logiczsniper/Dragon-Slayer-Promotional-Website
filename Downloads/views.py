from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Link

# Create your views here.
def index(request):
    all_links = Link.objects.all()
    template = loader.get_template("Downloads/index.html")
    context = {
        'all_links': all_links
    }
    return HttpResponse(template.render(context, request))
