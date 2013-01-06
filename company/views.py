# Create your views here.
from django.template import Context, loader
from company.models import Company
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,render_to_response

import json

def index(request):
   companies = Company.objects.all().exclude(Company_Display_Name__exact="").order_by('Company_Display_Name')
   return render_to_response('company/index.html', {'companies': companies})

def view(request,company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'company/view.html', {'company': company})