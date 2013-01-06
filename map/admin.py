from map.models import Location
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title','url','position')

admin.site.register(Location,LocationAdmin)
