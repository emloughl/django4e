from django.contrib import admin

from unesco.models import *

# Register your models here.
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Region)