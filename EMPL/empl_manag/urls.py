
from django.urls import path

from .views import EmpView,AttendanceView ,UpdateEmp,RemoveEmp,EmpbyID,GetAttendance
urlpatterns = [
  path("employee/emp_add/<int:emp_id>",EmpbyID.as_view(),name="emp_add_id"),
  path("employee/emp_add/", EmpView.as_view(), name="emp_add"),
#   path('employee/<int:pk>/', EmpView.as_view(), name='employee_detail'),
  path('employee/update_emp/<int:emp_id>', UpdateEmp.as_view() , name= "update_emp" ),
  path('employee/remove_emp/<int:emp_id>', RemoveEmp.as_view() , name= "remove_emp" ),
  path("employee/emp_add/add_attendance/<int:emp_id>/", AttendanceView.as_view(), name="add_attendance"),
  path('employee/', EmpView.as_view(), name='employee_list'),
  path("employee/emp_add/get_attendance/<int:emp_id>" ,GetAttendance.as_view(), name="get_attendance" ),

]
