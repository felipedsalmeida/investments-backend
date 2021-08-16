from django.db import models

# Create your models here.

class Sectors(models.Model):
    fid = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField()

    class Meta:
        unique_together = ['fid', 'slug']

    def __str__(self) -> str:
        return self.slug

class Companies(models.Model):
    cod=models.CharField(max_length=10,null=False)
    ycod=models.CharField(max_length=10,null=False)
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,auto_created=True)
    
    def __init__(self,cod):
        self.cod = cod

    def __str__(self) -> str:
        return self.cod

class StockResults(models.Model):
    cod=models.ForeignKey(Companies, on_delete=models.CASCADE)
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
        return self.cod + ',' + self.date
