# Create your views here.
from django.template import Context, loader
from company.models import Company,Comment
from map.models import Location
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,render_to_response

import json

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=200,required=True)
    email = forms.CharField(max_length=200,required=False)
    text = forms.CharField ( widget=forms.widgets.Textarea(),required=True )
    company_id = forms.CharField( widget=forms.widgets.HiddenInput() )


def index(request):
    locations = Location.objects.all()
    company_ids = set()
    for location in locations:
        if location.company_id != None:
            company_ids.add(location.company_id)
    companies = Company.objects.filter(id__in=company_ids).exclude(Company_Display_Name__exact="").order_by('Company_Display_Name')
    return render_to_response('company/index.html', {'companies': companies})

def view(request,company_id):
    company = get_object_or_404(Company, pk=company_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'company_id': company_id})
        if form.is_valid():
            #Process Form
            comment = Comment()
            comment.company_id = company_id
            comment.ip_address = request.META.get('REMOTE_ADDR')
            comment.email = form.cleaned_data['email']
            comment.name = form.cleaned_data['name']
            comment.text = form.cleaned_data['text']
            comment.save()
            #end
            form = CommentForm(initial={'company_id': company_id})
            return render(request, 'company/view.html', {'company': company, 'form' : form, 'submitted': True})
    else:
        form = CommentForm(initial={'company_id': company_id})
    return render(request, 'company/view.html', {'company': company, 'form' : form, 'submitted': False})