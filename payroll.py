class Employee:
    def __init__(self,id,name):
     self.id=id
     self.name=name

class SalaryEmployee(Employee):
    def __init__(self,name,id,basicSalary,Allowance):
     super().__init__(name,id)
     self.baicSalary=basicSalary
     self.Allowance=Allowance

class HourlyEmployee(Employee):
    def __init__(self,name,id,paymentHourly,hoursWorked):
        super().__init__(name,id)
        self.paymentHourly=paymentHourly
        self.hoursWorked=hoursWorked
        
    def calculate(self):
      print("total hourly pay="self.paymentHourly*self.hoursWorked)
        

class CommisionEmployee(SalaryEmployee):
   def __init__(self,name,id,sales,commision,basicSalary):
       super().__init__(name,id,basicSalary)
       self.sales=sales
       self.commision=commision
       
    def commisionCalculate(self)
    print("total salary="sales*commision+basicSalary)
    
    emp=Employee()
    emp=Employee("Alex","39862964")
    print(emp.name)
    print(emp.id)

