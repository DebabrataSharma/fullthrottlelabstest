from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.GenericDataList.as_view(), name='home'),
]
