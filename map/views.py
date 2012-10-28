# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from map.models import Location
from django.http import HttpResponse
import json

def index(request):
    t = loader.get_template('map/index.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

@csrf_exempt
def search(request):
    query = request.REQUEST['q']
    locations = Location.objects.filter(title__icontains=query)
    output = []
    for item in locations:
        output.append({'title':item.title,'url':item.url,'pos':[item.x_position,item.y_position]})
    return HttpResponse(json.dumps(output), mimetype="application/json")