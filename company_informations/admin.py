from django.contrib import admin
import fundamentus
from .models import Sectors

# Register your models here.

@admin.register(Sectors)
class SectorsAdmin(admin.ModelAdmin):
    model=Sectors
    list_display=('fid','name','slug')
    search_fields=('fid','name','slug',)
    ordering=['name']
    actions=['update_table']

    def update_table(self,request,queryset):
        sectors = fundamentus.setor._setor
        for s in sectors:
            try:
                Sectors.objects.create(slug=s[0],name=s[1],fid=s[2])
            except Exception as err:
                Sectors.objects.create(slug=s[0]+'2',name=s[1],fid=s[2])
                print(err)


