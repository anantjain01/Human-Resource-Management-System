from rest_framework import serializers
from .models import Emp ,Attendance
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        