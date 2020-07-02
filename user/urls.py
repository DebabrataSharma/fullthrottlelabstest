from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_data', views.create_dummy_data, name='create_dummy_data')
    

]
