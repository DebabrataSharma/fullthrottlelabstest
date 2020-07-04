from rest_framework import serializers
from .models import Users, ActivityPeriod
import datetime
import random
import pytz


class UserSerializer(serializers.ModelSerializer):
    activity_period = serializers.StringRelatedField(many=True)
    class Meta:
        model = Users
        
        fields = ['id','real_name','tz','activity_period']
    