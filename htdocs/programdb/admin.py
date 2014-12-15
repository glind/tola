from django.contrib import admin
from .models import Country, Province, Cluster, Village, Program

admin.site.register(Country)
admin.site.register(Province)
admin.site.register(Cluster)
admin.site.register(Village)
admin.site.register(Program)