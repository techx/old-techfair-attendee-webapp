# Create your views here.
from django.template import Context, loader
from company.models import Company
from django.http import HttpResponse
import json

def index(request):
    t = loader.get_template('company/index.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

def view(request,CompanyId):
    t = loader.get_template('company/view.html')
    c = Context({
    })
    return HttpResponse(t.render(c))