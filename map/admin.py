from map.models import Location
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title','url','x_position','y_position')

admin.site.register(Location,LocationAdmin)
