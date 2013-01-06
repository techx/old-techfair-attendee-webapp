# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from map.models import Location
from company.models import Company
from django.http import HttpResponse
from django.db.models import Q

import json

def index(request):
    t = loader.get_template('map/index.html')
    c = Context({
    })
    return HttpResponse(t.render(c))

@csrf_exempt
def search(request):
    query = request.REQUEST['q']
    companies = Company.objects.filter(Company_Display_Name__icontains=query)
    companies_id = []
    company_dict= {}
    for company in companies:
        companies_id.append(company.id)
        company_dict[company.id] = company
    locations = Location.objects.filter(Q(title__icontains=query) | Q(company_id__in=companies_id))
    output = []
    for item in locations:
        position = map(int, item.position.split(','))

        if item.company_id is not None:
            company = company_dict[item.company_id]
            output.append({'title':company.Company_Display_Name ,'description':company.Company_Description,'url': '/company/%d/' % item.company_id,'pos':position})
        else:
            output.append({'title':item.title,'description':item.description,'url':item.url,'pos':position})
    return HttpResponse(json.dumps(output), mimetype="application/json")