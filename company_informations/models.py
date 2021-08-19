from django.db import models

# Create your models here.

class Sector(models.Model):
    fid = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(unique=True)
    
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    cod=models.CharField(max_length=10,null=False,unique=True)
    ycod=models.CharField(max_length=10,null=False)
    name=models.CharField(max_length=255)
    sector=models.ForeignKey(Sector, on_delete=models.CASCADE)
    subsector=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_created=True,auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,auto_created=True)

    def __str__(self) -> str:
        return f'company:{self.cod}'

class CompanyOscillation(models.Model):
    cod=models.CharField(max_length=255)
    min_52_week=models.DecimalField(decimal_places=2,max_digits=5)
    max_52_week=models.DecimalField(decimal_places=2,max_digits=5)
    vol_med_2m=models.IntegerField()
    market_value=models.IntegerField()
    last_balance_process=models.DateField()
    nr_stocks=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,auto_created=True)
    
    def __str__(self) -> str:
        return f'oscillations:{self.cod}'

class MarketDayResult(models.Model):
    cod=models.CharField(max_length=255)
    date = models.DateTimeField()
    open=models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    close=models.FloatField()
    adj_close=models.FloatField()
    volume=models.IntegerField()
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_created=True,auto_now_add=True)

    def __str__(self) -> str:
        return 'stocks result: ' + self.cod + ',' + self.date
