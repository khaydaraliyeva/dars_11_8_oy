from .models import *
from rest_framework import serializers

class XarajatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xarajat
        fields = '__all__'
        