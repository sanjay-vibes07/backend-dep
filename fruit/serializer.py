from rest_framework.serializers import ModelSerializer
from .models import *
class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields =  "__all__"
        # fields =  ["name","salary"]