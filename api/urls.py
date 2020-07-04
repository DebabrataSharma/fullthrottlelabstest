from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('data', views.GenericDataList.as_view(), name='home'),
]
