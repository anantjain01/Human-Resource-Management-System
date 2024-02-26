from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField( max_length = 30,null=True)
    designation = models.CharField(max_length= 30, null=True)
    department = models.CharField( max_length = 40)
    doj = models.DateTimeField( auto_now_add =True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Emp, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {'Present' if self.present else 'Absent'}"