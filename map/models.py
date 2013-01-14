from django.db import models
from company.models import Company
# Create your models here.
class Location(models.Model):
    location= models.CharField(max_length=200)
    company = models.ForeignKey(Company,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    position = models.CharField(max_length=200,
        help_text="Visit /map/#TECHFAIRMAPDEBUG-IDONOTTHINKSOMEONECANACCIDENTALLYTYPETHISSENTENSEWITHOUTVIEWINGTHESOURCECODEORWITHLINK to get actual position ")