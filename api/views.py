from django.shortcuts import render, redirect
from .models import Users, ActivityPeriod
from django.views.decorators.csrf import csrf_exempt
import random
import pytz
import datetime
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics, mixins

# class GenericDataList(generics.GenericAPIView, mixins.ListModelMixin):
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()
#     renderer_classes = [JSONRenderer]

#     def get(self, request):
#         # user_data = Users.objects.all()
#         # context = {'user':user_data}
#         return self.list(request)

class GenericDataList(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        user_data = Users.objects.all()

        serializer = UserSerializer(user_data, many=True)
        if serializer.data:
            for each in serializer.data:
                if "activity_period" in each.keys():
                    for i in range(0,len(each['activity_period'])):
                        each['activity_period'][i] = eval(each['activity_period'][i])
            data = {"ok":"true", "members":serializer.data}
        else:
            data = {"ok":"false", "members": None}
        return Response(data)