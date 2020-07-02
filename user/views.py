from django.shortcuts import render, redirect
from .models import Users, ActivityPeriod
from django.views.decorators.csrf import csrf_exempt
import random
import pytz
import datetime
# Create your views here.
# @csrf_exempt
def home(request):
    if request.method=='GET':
        user = Users.objects.all()
        print(user,".................")
        context = {'user': user}
        for each_user in user:
            print(each_user.activity_period.all())
        return render(request, 'home.html', context)

@csrf_exempt
def create_dummy_data(request):

        real_name = request.POST.get('name')
        tz = random.choice(pytz.all_timezones)
        Users.objects.create(real_name=real_name, tz=tz)
        num_activity_periods = random.randint(0,4)
        for each_activity_period in range(0, num_activity_periods):
            start_time = datetime.datetime.today() - datetime.timedelta(days=random.randrange(8))
            end_time = start_time + datetime.timedelta(days=random.randrange(10))
            user = Users.objects.get(real_name=real_name)
            ActivityPeriod.objects.create(start_time=start_time,end_time=end_time, user=user)
        return redirect('user:home')
        

