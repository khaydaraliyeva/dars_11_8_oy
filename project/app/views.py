from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from .serializers import *
from .models import *

class XarajatViewSet(viewsets.ModelViewSet):
    serializer_class = XarajatSerializer

    def get_queryset(self):
        return Xarajat.objects.filter(user_id=self.request.user.id)
        
        
