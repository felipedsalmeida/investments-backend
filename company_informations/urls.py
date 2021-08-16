from django.urls import path

from . import views

app_name = 'company_informations'

urlpatterns = [
    path('', views.SectorsListView.as_view(), name='sectors'),
]