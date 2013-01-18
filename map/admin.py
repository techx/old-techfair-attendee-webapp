from map.models import Location
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location','company','title','description','url')

admin.site.register(Location,LocationAdmin)
