from django.shortcuts import render
# Create your views here.

from .models import Emp,Attendance
from rest_framework import status
from django.shortcuts import get_object_or_404
from empl_manag.serializers import EmpSerializer ,AttendanceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class EmpView(APIView):

    def get(self, request):
        employees = Emp.objects.all()
        serializer = EmpSerializer(employees, many=True)
        # return Response(serializer.data)
        return render(request, 'employee_list.html', {'employees': serializer.data})

    def post(self, request):
        serial = EmpSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({"success": "Data saved successfully"})
        else:
            return Response({"failure": "Serializer is not valid"})
        
class EmpbyID(APIView):
     def get(self, request,emp_id):
        employees = get_object_or_404(Emp, id = emp_id)
        serializer = EmpSerializer(employees)
        return Response(serializer.data)

class UpdateEmp(APIView):
    def put(self, request, emp_id):
        employee = get_object_or_404(Emp, id=emp_id)
        serializer = EmpSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Data updated successfully"})
        else:
            return Response({"failure": "Serializer is not valid", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RemoveEmp(APIView):
    def delete(self, request, emp_id):
        employee = get_object_or_404(Emp, id=emp_id)
        employee.delete()
        return Response({"success": "Data deleted successfully"})

class AttendanceView(APIView):
    def post(self, request, emp_id):
        employee = get_object_or_404(Emp, id=emp_id)
        attendance_serial = AttendanceSerializer(data=request.data)
        if attendance_serial.is_valid():
            attendance_serial.save()
            return Response({"success": "Attendance added successfully"})
        else:
            return Response({"failure": "Attendance serializer is not valid", "errors": attendance_serial.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetAttendance(APIView):
    def get( self, request, emp_id):
        employee = get_object_or_404(Emp, id=emp_id)

        # Query attendance for the specified employee
        attendances = Attendance.objects.filter(employee=employee)

        # Serialize the attendance data
        serializer = AttendanceSerializer(attendances, many=True)

        # return Response(serializer.data)
        return render(request, 'attendance.html', {'attendance': serializer.data})


