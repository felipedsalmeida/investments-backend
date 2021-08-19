import pandas as pd
from django.contrib import admin
from django.db.utils import IntegrityError
from pandas.core.frame import DataFrame
import fundamentus
from . import models

# Register your models here.

@admin.register(models.Sector)
class SectorAdmin(admin.ModelAdmin):
    model=models.Sector
    list_display=[field.name for field in model()._meta.fields]
    search_fields=[field.name for field in model()._meta.fields]
    ordering=['name']
    actions=['update_table']

    def update_table(self,request,queryset):
        sectors = fundamentus.setor._setor
        for s in sectors:
            try:
                self.model.objects.create(slug=s[0],name=s[1],fid=s[2])
            except Exception as err:
                self.model.objects.create(slug=s[0]+'2',name=s[1],fid=s[2])
                print(err)

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    model=models.Company
    list_display=[field.name for field in models.Company()._meta.fields]
    search_fields=['cod','name']
    ordering=['name']
    actions=['update_table']
    # list_per_page=25
    


    def update_table(self,request,queryset):
        companies_on_db = [i.cod for i in queryset]
        sectors = [i for i in models.Sector.objects.all()]
        errors = []
        for s in sectors:
            print('init make request companies info from setor {}...'.format(s.name))
            companies_codes = [i for i in fundamentus.list_papel_setor(s.fid) if i not in companies_on_db]
            if len(companies_codes) > 0:
                df = fundamentus.get_papel(companies_codes)
                df.columns = [i.lower() for i in df.columns]
                df = df.reset_index().rename(columns={'index':'cod'})
                print('request info success! init add data on db...')
                for i,r in df.iterrows():
                    try:
                        company = self.model(
                            cod=r.cod,
                            ycod=r.cod + '.SA',
                            name=r.empresa,
                            sector=s,
                            subsector=r.subsetor
                        )
                        company.save()
                    except IntegrityError as err:
                        errors += [str(err)]
                        print('Número de erros:',len(errors))
                        continue
                    

@admin.register(models.CompanyOscillation)
class CompanyOscillationAdmin(admin.ModelAdmin):
    model=models.CompanyOscillation
    list_display=[field.name for field in model()._meta.fields]


