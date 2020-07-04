"""module contains all the functions for frontend interaction"""
from django.shortcuts import render, redirect
from api.models import Users, ActivityPeriod
from django.views.decorators.csrf import csrf_exempt
import random
import string
import pytz
import datetime
import requests
from api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def home(request):
    """
    Url for home function.

    :http relative-url: /
    :http-method :GET
    """
    if request.method == 'GET':
        url = 'http://'+request.get_host()+'/api/data'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url=url, headers=headers)
        if response.json()['members']:
            context = {'user': response.json()}
        else:
            context = {'user': None}
        return render(request, 'home.html', context)

@csrf_exempt 
def create_dummy_data(request):
    """
    Function to populate database.

    :http relative-url: /create_data
    :http-method :POST
    """
    real_name = request.POST.get('name')
    tz = random.choice(pytz.all_timezones)
    letters = string.ascii_lowercase+'0123456789'
    id =  ''.join(random.choice(letters) for i in range(0,9))
    user = Users.objects.create(id=id,real_name=real_name, tz=tz)
    num_activity_periods = random.randint(0,4)
    for each_activity_period in range(0, num_activity_periods):
        start_time = datetime.datetime.today() - datetime.timedelta(days=random.randrange(8))
        end_time = start_time + datetime.timedelta(days=random.randrange(10))
        ActivityPeriod.objects.create(start_time=start_time,end_time=end_time, user=user)
    return redirect('user:home')
    

