class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

#Child class
class Employee_Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def executesDuty(self):
        print(self.name, "is managing",self.department,"department")
m1=Employee_Manager("Shafana",50000,"IT")
m1.show()
m1.executesDuty()
            
        
